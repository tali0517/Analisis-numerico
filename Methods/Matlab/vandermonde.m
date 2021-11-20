%Script designed to find the interpolating polynomial from 
% the given data by using Vandermonde's Method  

%Input:
%X: values of X for the data 
%Y: values for f(x) 

function x = vandermonde(X,Y)
n = length(X); 
A = zeros(n); 

for i=1:n
    A(:,i) = (X.^(n-i))';
    disp(A);
end
x = mldivide(A,Y'); 
end