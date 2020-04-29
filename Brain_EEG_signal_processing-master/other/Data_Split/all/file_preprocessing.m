testfiledir = 'E:\MachineLearning\TestFiles\';
matfiles = dir(fullfile(testfiledir, '*.txt'));
nfiles = length(matfiles);
data  = cell(nfiles);
for i = 1 : nfiles
   fid = fopen( fullfile(testfiledir, matfiles(i).name) );
   data{i} = fscanf(fid,'%c');
   fclose(fid);
end