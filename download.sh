cd autocorrection
mkdir input
mkdir input/luanvan
cd input/luanvan
gdown https://drive.google.com/uc?id=1WpsWHXkjp_qwySAxpBI5oxwA3t5m4wye
cd ../..

mkdir weights
mkdir weights/history
mkdir weights/model
cd weights/model
gdown https://drive.google.com/uc?id=1VH3C2wti6MbL7LODiABqBj5qXFEc7lQ_
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