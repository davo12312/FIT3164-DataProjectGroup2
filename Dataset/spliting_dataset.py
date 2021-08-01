
import os
import splitfolders


# to find directory
print(os.listdir())

# split dataset according to ratios
# input_folder = 'Input_Photos/'
# splitfolders.ratio(input_folder, output = 'Test_Output',
#                   seed=42, ratio=(.7, .0, .3),     # train, validation, test
#                   group_prefix = None)

# split dataset according to fixed numbers

input_folder = 'Input_Photos/'
splitfolders.fixed(input_folder, output='Output_Photos',
                   seed=42, fixed=(0,3000),   # training:7k, validation:0, testing:3k
                   oversample=False, group_prefix=None)

