%Program to find solution to linnear system Ax=b, with LU factorization 
%and Cholesky's method.

%Input:
%A: Invertible matrix 
%b: constant vector 

function [x,L,U] = LUCholesky(A,b)
n = size(A,1);
L = eye(n);
U = L;

for i=1:n-1
    L(i,i)=sqrt(A(i,i)-dot(L(i,1:i-1),U(1:i-1,i)'));
    U(i,i)=L(i,i);
    for j=i+1:n
        L(j,i)=(A(j,i)-dot(L(j,1:i-1),U(1:i-1,i)'))/U(i,i);
    end
    for j=i+1:n
        U(i,j)=(A(i,j)-dot(L(i,1:i-1),U(1:i-1,j)'))/L(i,i);
    end
    disp('Iteration # %d',i);
    disp(L);
    disp(U);
end
L(n,n)=sqrt(A(n,n)-dot(L(n,1:n-1),U(1:n-1,n)'));
U(n,n)=L(n,n);
disp('Final Upper triangle Matrix:')
disp(U);

z = progsust([L b]);
x = regrsust([U z]);
end