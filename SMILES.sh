if [ $# -eq 0 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

babel /Users/yashravipati/Downloads/PDBBind_processed/$1/$1_ligand.mol2 -osmi 
