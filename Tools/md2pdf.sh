#author alexshcer
#requirment: pandoc 

for i in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30; do
    cd ../Program-$i
    pwd
    pandoc --variable "geometry=margin=0.6in" --variable mainfont="Alata" --variable sansfont="Helvetica" --variable monofont="Menlo" README.md --from markdown-fancy_lists --pdf-engine=xelatex -o README.pdf
done