

cd /hpc/meca/data/Macaques/MyelinMaps/Left/
for sub in cerimed_cesar cerimed_jaffar ucdavis_032125 ucdavis_032126 ucdavis_032131 ucdavis_032132 ucdavis_032133 ucdavis_032134 ucdavis_032135 ucdavis_032136 ucdavis_032137 ucdavis_032138 ucdavis_032139 ucdavis_032140 ucdavis_032141 ucdavis_032142 ucdavis_032143
do
    /hpc/soft/brainvisa/brainvisa_4.6.0/bin/python /hpc/meca/users/coulon.o/localPythonDev/myelin-maps/projectT1T2onSurface.py no_norm/${sub}_t1divt2_cropped_nobias_zp.nii.gz Surfaces/${sub}_Lwhite_fine.gii no_norm/${sub}_myelin.gii
    /hpc/soft/brainvisa/brainvisa_4.6.0/bin/python /hpc/meca/users/coulon.o/localPythonDev/myelin-maps/projectT1T2onSurface.py norm/${sub}_t1divt2_cropped_nobias_zp.nii.gz Surfaces/${sub}_Lwhite_fine.gii norm/${sub}_myelin.gii
    


