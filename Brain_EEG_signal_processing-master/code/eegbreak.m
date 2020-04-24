x = load('HeadEEGSADopensignals_ecg2_201607182369_2020-02-01_23-42-16.txt')


Fs=256  %%sampling frequency

t=1/Fs;
S=x(:,6);
waveletFunction = 'db8';
[C,L] = wavedec(S,8,waveletFunction);

plot(S);


%% Calculating the coefficients vectors
cD1 = detcoef(C,L,1); %NOISY
cD2 = detcoef(C,L,2); %NOISY
cD3 = detcoef(C,L,3); %NOISY
cD4 = detcoef(C,L,4); %NOISY
cD5 = detcoef(C,L,5); %GAMA
cD6 = detcoef(C,L,6); %BETA
cD7 = detcoef(C,L,7); %ALPHA
cD8 = detcoef(C,L,8); %THETA
cA8 = appcoef(C,L,waveletFunction,8); %DELTA


%%%% Calculation the Details Vectors
D1 = wrcoef('d',C,L,waveletFunction,1); %NOISY
D2 = wrcoef('d',C,L,waveletFunction,2); %NOISY
D3 = wrcoef('d',C,L,waveletFunction,3); %NOISY
D4 = wrcoef('d',C,L,waveletFunction,4); %NOISY
D5 = wrcoef('d',C,L,waveletFunction,5); %GAMMA
D6 = wrcoef('d',C,L,waveletFunction,6); %BETA
D7 = wrcoef('d',C,L,waveletFunction,7); %ALPHA
D8 = wrcoef('d',C,L,waveletFunction,8); %THETA
A8 = wrcoef('a',C,L,waveletFunction,8); %DELTA



d6=D6(101:3100)
d7=D7(101:3100)
d8=D8(101:3100)


%%%plotting the alph, beta, gamma, theta etc

subplot(3,1,1)
plot(d6)  %%beta

subplot(3,1,2)
plot(d7)  %%alpha

subplot(3,1,3)
plot(d8)  %%theta




