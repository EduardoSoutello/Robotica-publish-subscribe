#include <ros/ros.h>
#include <std_msgs/String.h>

void callback_funcao(const std_msgs::String& msg){

        ROS_INFO("Mensagem: %s",msg.data.c_str());

}

int main(int argc, char **argv){
        ros::init(argc,argv,"escucomunicacao");

        ros::NodeHandle nh;

        ros::Subscriber sub = nh.subscribe("/comunicacao", 1000, callback_funcao);

        ros::spin();

}


