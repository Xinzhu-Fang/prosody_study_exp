stimuli_dir=/Users/xzfang/Github/stressTurk_tutorial/

# mkdir $stimuli_dir/men_women_images
# find $stimuli_dir/images_with_no_name \( -name "*Man*Woman*" -o -name "*Woman*Man*" \) -exec cp {} $stimuli_dir/men_women_images \;

# mkdir $stimuli_dir/men_boys_images
# find $stimuli_dir/images_with_no_name \( -name "*Man*Boy*" -o -name "*Boy*Man*" \) -exec cp {} $stimuli_dir/men_boys_images \;
#
# mkdir $stimuli_dir/men_girls_images
# find $stimuli_dir/images_with_no_name \( -name "*Man*Girl*" -o -name "*Girl*Man*" \) -exec cp {} $stimuli_dir/men_girls_images \;

# mkdir $stimuli_dir/boys_girls_images
# find $stimuli_dir/images_with_no_name \( -name "*Girl*Boy*" -o -name "*Boy*Girl*" \) -exec cp {} $stimuli_dir/boys_girls_images \;

# mkdir $stimuli_dir/women_girls_images
# find $stimuli_dir/images_with_no_name \( -name "*Girl*Woman*" -o -name "*Woman*Girl*" \) -exec cp {} $stimuli_dir/women_girls_images \;
#
# mkdir $stimuli_dir/boys_women_images
# find $stimuli_dir/images_with_no_name \( -name "*Woman*Boy*" -o -name "*Boy*Woman*" \) -exec cp {} $stimuli_dir/boys_women_images \;



mkdir $stimuli_dir/F_F_images
find $stimuli_dir/images_with_no_name \( -name "*Girl*Woman*" -o -name "*Woman*Girl*" \) -exec cp {} $stimuli_dir/F_F_images \;


mkdir $stimuli_dir/M_F_images
find $stimuli_dir/images_with_no_name \( -name "*Man*Woman*" -o -name "*Boy*Woman*" -o -name "*Man*Girl*" -o -name "*Boy*Girl*" \) -exec cp {} $stimuli_dir/M_F_images \;

mkdir $stimuli_dir/F_M_images
find $stimuli_dir/images_with_no_name \( -name "*Woman*Boy*" -o -name "*Woman*Man*" -o -name "*Girl*Boy" -o -name "*Girl*Man" \) -exec cp {} $stimuli_dir/F_M_images \;

mkdir $stimuli_dir/M_M_images
find $stimuli_dir/images_with_no_name \( -name "*Man*Boy*" -o -name "*Boy*Man*" \) -exec cp {} $stimuli_dir/M_M_images \;
