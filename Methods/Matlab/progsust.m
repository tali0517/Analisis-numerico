%Progressive substitution for an augmented Matrix A =[L,b]

function x = progsust(A)
n = size(A,1);
x = zeros(n,1);

x(1)=A(1,n+1)/A(1,1);  % Sets first value for var x = to b(1)/L(1,1)
for i=2:n
    temp = [1 x(i-1)']; 
    temp1 = [A(i,n+1) - A(i,1:i-1)]; 
    x(i) = dot(temp,temp1)/A(i,i);
end 
end 
