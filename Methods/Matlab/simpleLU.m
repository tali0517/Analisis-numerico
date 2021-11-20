%% LU Simple 

% Input 
% A = invertible matrix 
% b = constants vector 

% Output 
% Matrix 'L' from factorization 
% Matrix 'U' from factorization 

function [x,L,U] = simpleLU(A,b)

n = size(A,1); %Column size for vector A 
L = eye(n); %Identity Matrix 
U = zeros(n);
M = A;
                %                            |\
for i=1:n-1     %%Inferior Triangle for loop |_\
    for j=i+1:n
        if M(j,i) ~= 0
            L(j,i) = M(j,i)/M(i,i);
            M(j,i:n) = M(j,i:n) - (M(j,i)/M(i,i))*M(i,i:n);
            fprintf('Lower Triangle alteration:')
            disp(M); 
        end
    end
                                            
    %Upper triangle matrix alterations      
    U(i,i:n) = M(i,i:n);
    U(i+1,i+1:n) = M(i+1,i+1:n);
    fprintf('Upper Triangle Alteration')
    disp(U)

end
U(n,n)=M(n,n); 
fprintf('Final Matrix U');
disp(U); 
z = progsust([L b]);
x = regrsust([U b]);
end
