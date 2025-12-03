#include <ros/ros.h>

int main(int argc, char **argv){
        ros::init(argc,argv,"teste");
        ros::NodeHandle nh;
        while(1){
                ROS_INFO("Sou um node teste");

                ros::Duration(2.0).sleep();
        }

}
~                                                                               
~                                                                               
~                                                                               
~              
