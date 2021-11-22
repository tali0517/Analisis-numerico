%Script finds the interpolating polynomial from the given data
% using Lagrange's method. 

%Input: 
%X: values of X for the data 
%Y: values for f(x) 


function [L,x] = lagrange(X,Y)
n = length(X);
L = zeros(n);

for i=1:n
    temp = setdiff(X,X(i)); %Removes from X the i positioned value
    temp1 = 1 -temp(1);
    for j=2:n-1
        temp1 = conv(temp1,1-temp(j));
    end
    L(i,:) = temp1/polyval(temp1,X(i));
end
x = Y*L;

