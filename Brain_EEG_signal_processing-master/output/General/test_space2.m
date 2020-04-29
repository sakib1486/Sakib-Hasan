num = []
temp = []
for i=1:6
    for j=1:2000
        num = [num, i];
    end
    num = transpose(num)
    temp = [temp, num]
    num = []
end

temp



