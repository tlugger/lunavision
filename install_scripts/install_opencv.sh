
echo "Updating installed dependancies..."
echo "----------------------------------"
sudo apt update && sudo apt upgrade -y -q

echo "\n\nInstalling developer tools and CMake..."
echo "-------------------------------------------"
sudo apt install build-essential cmake pkg-config -y -q

echo "\n\nInstalling image I/O packages..."
echo "------------------------------------"
sudo apt install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev -y -q

echo "\n\nInstalling video I/O packages..."
echo "------------------------------------"
sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y -q
sudo apt install libxvidcore-dev libx264-dev -y -q

echo "\n\nInstalling GTK devlopment library prerequisites..."
echo "------------------------------------------------------"
sudo apt install libfontconfig1-dev libcairo2-dev -y -q
sudo apt install libgdk-pixbuf2.0-dev libpango1.0-dev -y -q
sudo apt install libgtk2.0-dev libgtk-3-dev -y -q

echo "\n\nInstalling matrix optimization packages..."
echo "----------------------------------------------"
sudo apt install libatlas-base-dev gfortran -y -q

echo "\n\nInstalling QT packages..."
echo "-----------------------------"
sudo apt install libhdf5-dev libhdf5-serial-dev libhdf5-103 -y -q
sudo apt install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 -y -q

echo "\n\nInstalling Python 3 header files..."
echo "---------------------------------------"
sudo apt install python3-dev -y -q

echo "\n\nInstalling remaining opencv-python dependancies..."
echo "------------------------------------------------------"
sudo apt install libtiff5 libpango-1.0-0 libavcodec58 libgdk-pixbuf2.0-0 libjasper1 libqt4-test libpangocairo-1.0-0 libswscale5 libilmbase23 libatk1.0-0 libgtk-3-0 libqtcore4 libcairo2 libwebp6 libavutil56 libcairo-gobject2 libopenexr23 libqtgui4 libavformat58 -y -q
