%Regressive substitution for an augmented Matrix A =[U,b]

function x = regrsust(A)
n = size(A,1);
x = zeros(n,1);

x(n)=A(1,n+1)/A(1,1);  % Sets first value for var x = to b(1)/U(1,1)
for i=n-1:-1:1
    temp = [1 x(i+1:n)']; 
    temp1 = [A(i,n+1) - A(i,i+1:n)]; 
    x(i) = dot(temp,temp1)/M(i,i);
end 
end 
