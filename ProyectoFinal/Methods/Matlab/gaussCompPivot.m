% Gaussian Elimination 
%Devolped by: Santiago Alzate, Sebastian Urrego, Esteban Sierra y Alejandro Castaño 
%Updated Last: 04/10/2021

%Inputs: 
%A = invertible matrix
%B = vector with independent terms 

%Output 
%ret, solution 

function x = gaussCompPivot(A,b)
C =[A,b'];

if n==m 
for i=1:n
    trace(i)=i;  
end
for k=1:n-1
    max=0;
    RowM=k; 
    ColM=k; 
    for p=k:n
        for r=k:n
            if max<abs(C(p,r))
                max=abs(C(p,r));
                RowM=p;
                ColM=r;
            end
        end
    end
    if max == 0
        fprintf('This system has infinte solutions!')
        break
    else
        if RowM ~= k
            for j=1:(n+1)
                aux=C(k,j);
                C(k,j)=C(RowM,j);
                C(RowM,j)=aux;
            end

        end
    if ColM ~= k
        for i=1:n
            aux=C(i,k);
            C(i,k)=C(i,ColM);
            C(i,ColM)=aux;
        end
        aux = trace(k);
        trace(k)= trace(ColM);
        trace(ColM)=aux;
    end
    end
for i=(k+1):n %scalar to set up the subtraction. 
    m(i,k)=C(i,k)/C(k,k); 
    for j=k:(n+1)
        C(i,j)= C(i,j) - m(i,k)*C(k,j); %Resulting Row 
    end
end
disp(C)
end
trace(ColM) = aux;
for i=n:-1:1
    suma=0;
    for p=(i+1):n
        suma = suma + C(i,p)*X(p);
    end
    X(i)=(C(i,n+1)-suma)/C(i,i);
end

%Reorganization of the matrix through the trace vector created. 
for i=1:n
    for j=1:n
        if trace(j)==i
            k=j;
        end
    end
    aux=X(k);   
    X(k)=X(i);
    X(i)=aux;
    aux=trace(k);
    trace(k)=trace(i);
    trace(i)=aux;
end
else 
    disp('Matrix is not squared: nxn');
end
