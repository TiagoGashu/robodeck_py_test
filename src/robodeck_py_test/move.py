#!/usr/bin/env python
import rospy
from robodeck_msgs.srv import connect
from robodeck_msgs.srv import move
from robodeck_msgs.srv import disconnect

def connectFunction():
	rospy.wait_for_service('robodeck/connect')
	try:
		connect_proxy = rospy.ServiceProxy('robodeck/connect', connect)
		ans = connect_proxy('192.168.0.1', 2000)
		return ans.isConnected
	except Exception, e:
		raise e

def moveFunction():
	rospy.wait_for_service('robodeck/move')
	try:
		move_proxy = rospy.ServiceProxy('robodeck/move', move)
		ans = move_proxy(32767)
		return ans.executed
	except Exception, e:
		raise e

def disconnectFunction():
	rospy.wait_for_service('robodeck/disconnect')
	try:
		disconnect_proxy = rospy.ServiceProxy('robodeck/disconnect', disconect)
		ans = disconnect_proxy()
		return ans.isDisconnected
	except Exception, e:
		raise e

if __name__ == '__main__':
	try:
		if(connectFunction()):
			print 'conectou-se ao robo'
			if(moveFunction()):
				print 'O robo movimentou-se'
			if(disconnectFunction()):
				print 'Desconectou-se do robo'
			else:
				print 'Problema ao tentar desconectar-se'
		else:
			print 'problema ao tentar enviar o comando de conexao'
	except Exception, e:
		raise e