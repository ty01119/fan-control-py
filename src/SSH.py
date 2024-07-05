import paramiko
import logging

class SSH:
  def __init__(self):
    pass

  def get_ssh_connection(self, ssh_machine, ssh_username, ssh_password, ssh_port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ssh_machine, username=ssh_username, password=ssh_password, timeout=10, port=ssh_port)
    return client
      
  def run_sudo_command(self, ssh_username="root", ssh_password="abc123", ssh_machine="localhost", ssh_port=22, command="ls", jobid="None"):
    conn = self.get_ssh_connection(ssh_machine=ssh_machine, ssh_username=ssh_username, ssh_password=ssh_password, ssh_port=ssh_port)
    command = "sudo -S -p '' %s" % command
    logging.info("Job[%s]: Executing: %s" % (jobid, command))
    stdin, stdout, stderr = conn.exec_command(command=command)
    stdin.write(ssh_password + "\n")
    stdin.flush()
    stdoutput = [line for line in stdout]
    stderroutput = [line for line in stderr]
    for output in stdoutput:
      logging.info("Job[%s]: %s" % (jobid, output.strip()))
    # Check exit code.
    logging.debug("Job[%s]:stdout: %s" % (jobid, stdoutput))
    logging.debug("Job[%s]:stderror: %s" % (jobid, stderroutput))
    logging.info("Job[%s]:Command status: %s" % (jobid, stdout.channel.recv_exit_status()))
    if not stdout.channel.recv_exit_status():
      logging.info("Job[%s]: Command executed." % jobid)
      conn.close()
      if not stdoutput:
        stdoutput = True
      return True, stdoutput
    else:
      logging.error("Job[%s]: Command failed." % jobid)
      for output in stderroutput:
        logging.error("Job[%s]: %s" % (jobid, output))
      conn.close()
      return False, stderroutput
