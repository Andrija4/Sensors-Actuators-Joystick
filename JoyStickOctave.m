clear all
close all
% Ensure you have the instrument-control package installed and loaded
pkg load instrument-control

% Define threshold values
LEFT_THRESHOLD = 400;
RIGHT_THRESHOLD = 800;
UP_THRESHOLD = 400;
DOWN_THRESHOLD = 800;

baud_rate = 9600;

serialportlist("avalibe")

s = serial("COM5", 9600);

pause(2);


% Create a figure and an initial plot
h = figure;
hold on;
x = 0;
y = 0;
dot = plot(x, y, 'ro'); % Initial position of the dot

% Main loop to update the dot position
while ishandle(h) % Continue running while the figure is open
    % Read joystick values

    flushinput(s);
    pause(0.005);
    temp = readline(s);


    if regexp(temp, "x: ")
      temp = temp(4:end);
      xValue = str2double(temp);
      yValue = nan;
    elseif regexp(temp, "y: ")
      temp = temp(4:end);
      yValue = str2double(temp);
      xValue = nan;
    else
      xValue = nan;
      yValue = nan;

    end

    disp(xValue);
    disp(yValue);

##    if isnan(xValue) || isnan(yValue)
##        continue; % Skip the loop iteration if the values are invalid
##    end

    % Update dot position based on joystick input
    if xValue < LEFT_THRESHOLD
        x = x - 10; % Move left
    elseif xValue > RIGHT_THRESHOLD
        x = x + 10; % Move right
    end

    if yValue < UP_THRESHOLD
        y = y + 10; % Move up
    elseif yValue > DOWN_THRESHOLD
        y = y - 10; % Move down
    end

    % Update the dot position on the graph
    set(dot, 'XData', x, 'YData', y);
    axis([-100 100 -100 100]); % Set axis limits
    drawnow; % Update the plot immediately

    % Add a small pause to avoid overwhelming the CPU
    pause(0.01);
end

% Close serial connection
fclose(s);
delete(s);
clear s;
