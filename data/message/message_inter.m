[p,S] = polyfit(x,y,1);
x_plus = linspace(0,105);
[y_fit,delta] = polyval(p,x_plus,S);
plot(x,y,'.b','markerSize',15)
hold on
plot(x_plus,y_fit,'r-')
plot(x_plus,y_fit+2*delta,'m--',x_plus,y_fit-2*delta,'m--')
legend({'message vs. n',['message = ', num2str(p(1)), ' * n + ', num2str(p(2))], '95% Prediction Interval'},'Location','best')
set(gca,'FontSize',16);
xlim([0 105]);
grid on;
xlabel('n') 
ylabel('message') 