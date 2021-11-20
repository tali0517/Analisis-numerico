%Program to find solution to linear system Ax=b, with LU factorization 
%and partial pivoting. 

%Input:
%A: Invertible matrix 
%b: constant vector 

function [x,L,U,P] = partLU(A,b)
n = size(A,1);
L = eye(n);
U = zeros(n);
P = L;
M = A; 

for i=1:n-1
    [aux0,aux]=max(abs(M(i+1:n,i))); %Aux0 is the greatest value in the first column for the first iteration. 
    if aux0>abs(M(i,i))
        disp(' ')
        aux2=M(i+aux,i:n);
        aux3=P(i+aux,:);
        M(aux+i,i:n)=M(i,i:n);
        P(aux+i, :) = P(i,:);
        M(i,i:n) = aux2;
        P(i,:) = aux3;
        if i>1
            aux4 = L(i+aux,1:i-1);
            L(i+aux,1:i-1) = L(i,1:i-1);
        end
    end
    for j=i+1:n
        if M(j,i)~=0
            L(j,i)=M(j,i)/M(i,i);
            M(j,i:n)=M(j,i:n)-(M(j,i)/M(i,i))*M(i,i:n);
        end
    end
    U(i,i:n)=M(i,i:n);
    U(i+1,i+1:n)=M(i+1,i+1:n);
end
U(n,n)=M(n,n);
fprintf('Final Matrix U');
disp(U);

z = progsust([L P*b]);
x = regrsust([U z]);
end 
