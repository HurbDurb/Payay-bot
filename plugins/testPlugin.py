import Bot;
import socket;

def init(config, curFolder):
    global server;
    global port;
    global nick;
    global passw;
    global channel;

    server = "irc.twitch.tv";
    port = 6667;
    nick = "USERNAME";
    passw = "oauth:Kappa";
    channel = "#notme";

    Bot.ircObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    Bot.ircObject.connect((server, port));

    Bot.ircObject.send("PASS " + passw + "\n");
    Bot.ircObject.send("NICK " + nick + "\n");
    Bot.ircObject.send("USER " + nick + "\n");
    Bot.ircObject.send("JOIN " + channel + "\n");

def tick():
    Bot.ircObject.settimeout(1.0/30);
    try:
        msg = Bot.ircObject.recv(1024);
    except socket.error, e:
        return 0;
    print(msg);
    print("dd");

    if msg.find(":Hoi " + nick) != -1:
        Bot.ircObject.send("PRIVMSG " + channel + " :HI!\n");
        print("SEND MSG!");

    if msg.find("PING") != -1:
        Bot.ircObject.send("PONG :Pong\n");
        print("PINGED!!!!!!");
