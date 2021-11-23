% Gaussian Elimination 
%Devolped by: Santiago Alzate, Sebastian Urrego, Esteban Sierra y Alejandro Castaño 
%Updated Last: 04/10/2021

%Inputs: 
%A = invertible matrix
%B = vector with independent terms 

%Output 
%ret, solution 

function ret = gaussElimination(A,B)

for col = 1:n - 1
    for row = col+1:nargin
        factor = A(row,col)/A(col,col);
        A(row,:) = A(row,:) - faactor*A(col,:);
        B(row) = B(row) - factor*B(col);
        c = [num2str(A), T, num2str(B)];
        disp(c);
        disp(newline);
    end
end
disp(ret)