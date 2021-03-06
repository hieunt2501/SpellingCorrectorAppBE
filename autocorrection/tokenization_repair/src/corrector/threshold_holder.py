from enum import Enum

from autocorrection.tokenization_repair.src.settings import paths
from autocorrection.tokenization_repair.src.helper.files import file_exists
from autocorrection.tokenization_repair.src.helper.pickle import load_object, dump_object


class ThresholdType(Enum):
    INSERTION_THRESHOLD = 0
    DELETION_THRESHOLD = 1


class FittingMethod(Enum):
    GREEDY = 0
    SINGLE_RUN = 1
    TWO_PASS = 2
    LABELING = 3


THRESHOLD_FILES = {
    FittingMethod.GREEDY: paths.DECISION_THRESHOLD_FILE,
    FittingMethod.SINGLE_RUN: paths.SINGLE_RUN_DECISION_THRESHOLD_FILE,
    FittingMethod.TWO_PASS: paths.TWO_PASS_DECISION_THRESHOLD_FILE,
    FittingMethod.LABELING: paths.LABELING_DECISION_THRESHOLD_FILE
}


def _names_set_correctly(model_name, fwd_model_name, bwd_model_name):
    if model_name is None:
        return fwd_model_name is not None and bwd_model_name is not None
    else:
        return fwd_model_name is None and bwd_model_name is None


def _key(model_name, fwd_model_name, bwd_model_name, noise_type):
    if not _names_set_correctly(model_name, fwd_model_name, bwd_model_name):
        raise Exception("Either model_name or fwd_model_name and bwd_model_name must be set.")
    if model_name is not None:
        return model_name, noise_type
    else:
        return fwd_model_name, bwd_model_name, noise_type


class ThresholdHolder:
    def __init__(self,
                 fitting_method: FittingMethod = FittingMethod.GREEDY,
                 autosave: bool = True):
        self.file = THRESHOLD_FILES[fitting_method]
        if file_exists(self.file):
            self.threshold_dict = load_object(self.file)
        else:
            print("WARNING: could not locate %s. A new, empty decision threshold dictionary was created instead."
                  % self.file)
            self.threshold_dict = dict()
        self.autosave = autosave

    def get_thresholds(self, model_name=None, fwd_model_name=None, bwd_model_name=None, noise_type=None):
        key = _key(model_name, fwd_model_name, bwd_model_name, noise_type)
        return self.threshold_dict[key]

    def save(self):
        dump_object(self.threshold_dict, self.file)

    def _set_threshold(self, model_name, fwd_model_name, bwd_model_name, noise_type, threshold, index):
        assert(threshold is not None)
        key = _key(model_name, fwd_model_name, bwd_model_name, noise_type)
        if key not in self.threshold_dict:
            self.threshold_dict[key] = [-1, -1]
        self.threshold_dict[key][index] = threshold
        if self.autosave:
            self.save()

    def set_threshold(self, threshold_type: ThresholdType, model_name=None, fwd_model_name=None, bwd_model_name=None,
                      threshold=None, noise_type=None):
        self._set_threshold(model_name, fwd_model_name, bwd_model_name, noise_type, threshold, threshold_type.value)

    def set_insertion_threshold(self, model_name=None, fwd_model_name=None, bwd_model_name=None, threshold=None,
                                noise_type=None):
        self.set_threshold(ThresholdType.INSERTION_THRESHOLD,
                           model_name=model_name,
                           fwd_model_name=fwd_model_name,
                           bwd_model_name=bwd_model_name,
                           threshold=threshold,
                           noise_type=noise_type)

    def set_deletion_threshold(self, model_name=None, fwd_model_name=None, bwd_model_name=None, threshold=None,
                               noise_type=None):
        self.set_threshold(ThresholdType.DELETION_THRESHOLD,
                           model_name=model_name,
                           fwd_model_name=fwd_model_name,
                           bwd_model_name=bwd_model_name,
                           threshold=threshold,
                           noise_type=noise_type)
