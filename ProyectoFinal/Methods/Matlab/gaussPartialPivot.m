% Gaussian Elimination 
%Devolped by: Santiago Alzate, Sebastian Urrego, Esteban Sierra y Alejandro Castaño 
%Updated Last: 04/10/2021

%Inputs: 
%A = invertible matrix
%B = vector with independent terms 

%Output 
%ret, solution 

function x = gaussPartialPivot(A,b)
[m, n] = size(A);
x = zeros(m,1);
l = zeros(m:m-1);


for col = 1:m-1

    for p = col+1:m
        if(abs(A(col,col)) < abs(A(p,col)))
            %Partial pivoting, switching rows. 
            A([col p],:) = A([p col], :);
            b([k p]) = b([p k]);
        end
    end

    for i = col+1:m
        l(i,col) = A(i,col)/A(col,col);
        for j = col+1:n
            A(i,j) = A(i,j)-l(i,col)*A(col,j);
        end
        b(i) = b(i)-l(i,col)*b(col);
    end

    disp([A B'])
end
for col = 1:m-1
    for i = col+1:m
        A(i,col) = 0;
    end
end

x(m) = b(m)/A(m,m);

for i = m-1:-1:1
    sum = 0;
    for j = i+1:m
        sum = sum + A(i,j)*x(j);
    end
    x(i) = (b(i) - sum)/A(i,i);
end
