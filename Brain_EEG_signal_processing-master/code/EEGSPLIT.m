%write the starting and ending position
start_pos = 39680
end_pos = 39790

%write the experiment state and the count (calculation / happy / sad )
state = 'calculation' 
count = '1'

%calculation (0, 1, 2, .....)
%happy(0, 1, 2, .....)


%write the first three letters of your name
my_name_3 = 'tan'

%write the name of the file (subject) you want to load
load_file_name = '1.txt'


%%%Don't edit unless you know what you are doing
load_file_name_nofmt = '1'
file_name = strcat(state,'_', load_file_name_nofmt, '_', my_name_3, '_',count)
file_name_csv = strcat(file_name,'.csv')
file_name_png = strcat(file_name,'.png')

x = load(load_file_name)

S=x(:,6);

s = S(start_pos:end_pos)
csvwrite(file_name_csv,s, 0, 0)

%%csvwrite('a.csv',s,0,0)

plot(s);

xlim([-50 1041])
ylim([-46 1045])
print(gcf,file_name_png,'-dpng','-r600');  
