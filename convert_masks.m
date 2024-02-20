clc;
clear;


mask_dir = 'PixelLabelData';
mask_files = dir(fullfile(mask_dir, '*.png'));
Destination_dir = 'ConvertedLabelData';
if ~exist(Destination_dir, 'dir')
       mkdir(Destination_dir)
end

for idx = 1:length(mask_files)
    load_FileName = mask_files(idx).name;
    image = imread(strcat(strcat(mask_dir,'\'), load_FileName));
    BW = imbinarize(image);
    imwrite(BW, strcat(strcat(strcat(Destination_dir,'\'), 'conv_'), ...
        load_FileName));
    fprintf(strcat('conv_', load_FileName + "\n"));
end
