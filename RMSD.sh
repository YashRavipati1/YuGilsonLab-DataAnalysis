if [ $# -eq 0 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

python RMSD.py "/Users/yashravipati/Downloads/PDBBind_processed/7gch/7gch_docked.pdbqt" "/Users/yashravipati/Downloads/RCSBpdbs/7gch.pdb"