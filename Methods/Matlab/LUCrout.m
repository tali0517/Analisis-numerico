% %Program to find solution to linear system Ax=b, with LU factorization 
%and Crout's method.

%Input:
% A: Invertible Matrix 
% b: Constants vector 

function [x,L,U] = LUCrout(A,b)
n = size(A,1);
L = eye(n);
U = L;

for i=1:n-1
    for j=1:n
        L(j,i) = A(j,i)-dot(L(j,1:i-1),U(1:i-1,i)');
    end
    for j=1+1:n
        U(i,j) = (A(i,j)-dot(L(i,1:i-1),U(1:i-1,j)'))/L(i,i);
    end
end

L(n,n)=A(n,n) - dot(L(n,1:n-1),U(1:n-1,n)');
disp('Final Lower Triangle Matrix:')
disp(L);

z = progsust([L b]);
x = regrsust([U z]);
end
