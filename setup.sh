python -m pip install -e .
# python -m pip install torch==1.11.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

cd autocorrection
mkdir input
mkdir input/luanvan
cd input/luanvan
gdown https://drive.google.com/uc?id=145geEupadzGwxZaueZE-kr4fHYmO-REC
cd ../..

mkdir weights
mkdir weights/history
mkdir weights/model
cd weights/model
gdown https://drive.google.com/uc?id=1PqGIjiQCp5xNINsAcBzOracLw0t6CuVA
cd ../..

cd tokenization_repair
mkdir data
mkdir data/estimators/
mkdir data/estimators/bilabel
mkdir data/estimators/lm/
mkdir data/estimators/lm/unilm
cd data/estimators/bilabel
gdown https://drive.google.com/drive/folders/1zhtQmPTah7qneEHPHuFHuf3qd5R047-W -O ./ --folder
cd ../lm/unilm
gdown https://drive.google.com/drive/folders/1lG3swcUyUPYOf4ziJGfPQboaYtD5SgTM -O ./ --folder
cd ../../../../../..