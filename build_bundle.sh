BASE_DIR=$(pwd)
mkdir -p bundle
cd validation
rm -f bundle.tar.gz
rm -f bundle/bundle.tar.gz
opa test . -v
opa build  --ignore tests --ignore input.json --output $BASE_DIR/bundle/bundle.tar.gz . 