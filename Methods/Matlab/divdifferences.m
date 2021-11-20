%Script finds the interpolating polynomial from the given data
% using the devided diferences method. 

%Input: 
%X: values of X for the data 
%Y: values for f(x) 

function x = divdifferences(X,Y)
n = length(X);
D = zeros(n);
D(:,1) = Y'; %Sets the first row for matrix D equal to the values in Y. 

for i = 2:n 
    temp = D(i-1:n,i-1);
    temp1 = diff(temp);
    temp2 = X(i:n)-X(1:n-i+1);
    D(i:n,i)= temp1./temp2';
    disp(D);
end
x = diag(D);