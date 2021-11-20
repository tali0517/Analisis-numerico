%Script finds the interpolating polynomial from the given data
% using Lagrange's method. 

%Input: 
%X: values of X for the data 
%Y: values for f(x) 

function x = linealspline(X,Y)
n = length(X);
m = 2*(n-1);
A = zeros(m);
b = zeros(m,1);
x = zeros(n-1,2);

for i=1:n-1
    A(i+1,[2*i-1 2*i])=[X(i+1) 1];
    b(i+1) = Y(i+1);  
end
A(1,[1 2])=[X(1) 1];
b(1) = Y(1);

disp('Interpolation Matrix after set up.')
disp(A);
disp(b);

for i=2:n-1
    A(n-1+i, 2*i-3:2*i) = [X(i) 1 -X(i) -1];
    b(n-1+i)=0;
end
disp('Matrix after ')

solve = mldivide(A,b);

for i=1:n
    x(i,:)=solve([2*i-1 2*i]);
end
end