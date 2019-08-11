file = importdata("data.csv");
data = file.data;
%% figure
figure('Renderer','zbuffer','Color',[1 1 1]);
color = (data(:,10)-min(data(:,10)))/(max(data(:,10))-min(data(:,10)));
S = repmat([20],numel(data(:,10)),1);
C = repmat([0.3],numel(data(:,10)),1);
scatter3(data(:,1),data(:,2),data(:,9),S,color);
shading interp;light;lighting gouraud;
colormap([10  0  0; 0  0  10]);
axis normal ;
xlabel('P');ylabel('T');zlabel('x_N2');