find /Users/yashravipati/Downloads/PDBBind_processed -type f -print0 | while IFS= read -r -d '' filename; do
    if [[ $filename == *.pdb ]]; then
        subdirectory=$(dirname "$filename")
        base=`basename $filename .pdb`
        obabel -ipdb $filename -opdbqt -O $subdirectory/$base.pdbqt
        echo $base
    else
        continue
    fi

done