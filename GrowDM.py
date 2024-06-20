import datetime
import os
import re
import signal
import socket
import sys
import threading
import warnings
import logging

# check if the date is less than the 30th of june 2024
if datetime.datetime.now() > datetime.datetime(2024, 6, 30):
    print("Prova gratuita scaduta...")
    input()
    sys.exit(1)

logging.Logger("WDM",50)
logging.disable()
from proxy_checking import proxy_checking

from tkinter import *; # type: ignore
import psutil
import boto3

warnings.simplefilter("ignore")
import Style as Style_
import base64
import ctypes
import json
import locale
import random
import ctypes as ct
import time
import traceback
from dataclasses import dataclass
from threading import Thread
from tkinter import filedialog, messagebox, simpledialog
from tkinter.ttk import *;
import requests
from instagrapi import Client, exceptions
from pandas import read_csv, read_excel
from phone_iso3166 import country
import boto3.session

def get_instance_public_ip_(ec2, instance_id):
    # Get the instance's metadata
    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]

    # Get the public IP address
    public_ip = instance['PublicIpAddress']

    return public_ip
import time

def stop_instances(ec2, instance_ids):
    try:
        # Get a list of running instances
        response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}],
            InstanceIds=instance_ids
        )

        # Stop the running instances
        running_instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                running_instances.append(instance['InstanceId'])
        if len(running_instances)>0:
            ec2.stop_instances(InstanceIds=running_instances)

    except Exception as e:
        return False

    return True


def get_instance_public_ip(ec2, ec2Resource, instance_id):
    # Start the instance
    ec2.start_instances(InstanceIds=[instance_id])

    # Wait until the instance is running
    try: 
        instance = ec2Resource.Instance(instance_id)
        instance.wait_until_running()
        time.sleep(10)
        if instance.public_ip_address is not None:
            return instance.public_ip_address
    except:time.sleep(60)

    # Wait 10 seconds
    time.sleep(10)

    # Get the instance's metadata
    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]

    # Get the public IP address
    public_ip = instance['PublicIpAddress']

    return public_ip

def start_instance(ec2, ec2Resource, instance_id):
    # Try to get the public IP address up to 5 times
    for i in range(5):
        public_ip = get_instance_public_ip(ec2, ec2Resource, instance_id)
        if public_ip is not None:
            return public_ip

    return None

def get_stopped_instances(ec2_client):
    # Use the describe_instances method to get a list of all instances
    response = ec2_client.describe_instances()

    # Initialize an empty list to store the instance IDs
    instance_ids = []

    # Iterate through the list of reservations
    for reservation in response["Reservations"]:
        # Get the list of instances in the reservation
        instances = reservation["Instances"]

        # Iterate through the list of instances
        for instance in instances:
            # Check if the instance is in a stopped state
            if instance["State"]["Name"] == "stopped":
                # If the instance is stopped, add its ID to the list
                instance_ids.append(instance["InstanceId"])

    # Return the list of stopped instance IDs
    return instance_ids

#Random code generation
def random__(*args,**kwargs):
    return random.randint(100000,999999)
def isvalidEmail(email):
    pattern = r"^\S+@\S+\.\S+$" # type: ignore
    objs = re.search(pattern, email)
    try:
        if objs!=None:
            if objs.string == email:
                return True
        else:
            return False
    except:
        return False
@dataclass()
class Settings:
    DmsAccount:int
    accountPath:str
    message:str
    comment:str
    receivers:"list[str]"
    loginTiming:int
    banTiming:int
    cycleTiming:int
    dmTiming:int
    followTiming:int
    likeTiming:int
    limitTiming:int
    commentTiming:int
    proxies:"list[str|None]"
    profile:"list[str|None]"
    post:"list[str|None]"
    story:"list[str|None]"
    updateData:"dict[str,str|None]"
    timezone:int
    locale:str
    country:str
    country_code:int
    app_version:str
    model:str
    os_version:str
    scale:str
    resolution:str
    position:str
    userAgent:str
    android:bool
    browser:bool
    storyAsSeen:bool
    likeStory:bool
    likePost:bool
    sendMessage:bool
    sendComment:bool
    inputCode:bool
    loginByBrowser:bool
    downloadUser:bool
    saveCookies:bool
    saveScreenshot:bool
    approveLogin:bool
    closeFriends:bool
    replyStoryAsDm:bool
    exploreReels:bool
    searchBeforeDm:bool
    followBeforeDm:bool
    randomRequests:bool
    createGroup:bool=False
    shutDown:bool=False
    closeDown:bool=False
    noCookies:bool=False

from types import FunctionType;
from selenium.webdriver import Chrome,ChromeOptions;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.chrome.service import Service;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOG'] = '0'
import io
from collections import UserString
from contextlib import redirect_stdout

class capture(UserString, str, redirect_stdout):
    '''
    Captures stdout (e.g., from ``print()``) as a variable.

    Based on ``contextlib.redirect_stdout``, but saves the user the trouble of
    defining and reading from an IO stream. Useful for testing the output of functions
    that are supposed to print certain output.
    '''

    def __init__(self, seq='', *args, **kwargs):
        self._io = io.StringIO()
        UserString.__init__(self, seq=seq, *args, **kwargs)
        redirect_stdout.__init__(self, self._io)
        return

    def __enter__(self, *args, **kwargs):
        redirect_stdout.__enter__(self, *args, **kwargs)
        return self

    def __exit__(self, *args, **kwargs):
        self.data += self._io.getvalue()
        redirect_stdout.__exit__(self, *args, **kwargs)
        return

    def start(self):
        self.__enter__()
        return self

    def stop(self):
        self.__exit__(None, None, None)
        return


class App:
    client:Client
    def darkTitleBar(self,win:"Tk|Toplevel"=None):
        pass
    def setTheme(self) -> None:
        pass
    #Start App with settings definition and thread
    def __init__(self) -> None:
        self.locale="en_us"
        try:
            if os.path.exists("GrowDMFiles"):
                if not os.path.isdir("GrowDMFiles"):
                    os.mkdir("GrowDMFiles")
            else:
                os.mkdir("GrowDMFiles")
            self.base_dir="GrowDMFiles/"
        except:
            self.base_dir="./"
        try:
            self.logdir="Logs"
            if os.path.exists("Logs"):
                if not os.path.isdir("Logs"):
                    os.mkdir("Logs")
            else:
                os.mkdir("Logs")
            self.dm_log="Logs/messages.csv"
            if not os.path.exists(self.dm_log):
                open(self.dm_log,"w").write("sep=;\nSender;Time;Num;Receiver;user-id\n")
            self.users_not_found_log="Logs/users-not-found.csv"
            if not os.path.exists(self.users_not_found_log):
                open(self.dm_log,"w").write("sep=;\nSender;Time;Num;Receiver;user-id\n")
            self.like_log="Logs/likes-sent.csv"
            if not os.path.exists(self.like_log):
                open(self.like_log,"w").write("sep=;\nSender;Time;Num;Receiver\n")
            self.comment_log="Logs/comment-sent.csv"
            if not os.path.exists(self.comment_log):
                open(self.comment_log,"w").write("sep=;\nSender;Time;Num;Receiver\n")
            self.storyview_log="Logs/story-viewed.csv"
            if not os.path.exists(self.storyview_log):
                open(self.storyview_log,"w").write("sep=;\nSender;Time;Num;Receiver\n")
            self.activity_log="Logs/account-activity.csv"
            if not os.path.exists(self.activity_log):
                open(self.activity_log,"w").write("sep=;\nUser;Time;Type|Json Response or Status\n")
        except:
            self.logdir="."
            self.dm_log="./messages.csv"
            if not os.path.exists(self.dm_log):
                open(self.dm_log,"w").write("sep=;\nSender;Time;Num;Receiver\n")
            self.users_not_found_log="./users-not-found.csv"
            if not os.path.exists(self.users_not_found_log):
                open(self.dm_log,"w").write("sep=;\nSender;Time;Num;Receiver;user-id\n")
            self.like_log="./likes-sent.csv"
            if not os.path.exists(self.like_log):
                open(self.like_log,"w").write("sep=;\nSender;Time;Num;Receiver\n")
            self.comment_log="./comment-sent.csv"
            if not os.path.exists(self.comment_log):
                open(self.comment_log,"w").write("sep=;\nSender;Time;Num;Receiver\n")
            self.storyview_log="./story-viewed.csv"
            if not os.path.exists(self.storyview_log):
                open(self.storyview_log,"w").write("sep=;\nSender;Time;Num;Receiver\n")
            self.activity_log="./account-activity.csv"
            if not os.path.exists(self.activity_log):
                open(self.activity_log,"w").write("sep=;\nUser;Time;Type\n")
        self.app_version:str="203.0.0.29.118"
        self.model:str="iPhone14,5"
        self.os_version:str="iOS 15_6_1"
        self.scale:str="3.00"
        self.resolution:str="1170x2532"
        self.position:str="NW/3"
        self.timezone=time.timezone
        self.proxy_list=[]
        self.is_closed=False
        self.publish_story=[]
        self.publish_post=[]
        self.picture=[]
        self.log=[]
        try:
            self.blacklist=open(self.base_dir+"blacklist.txt",encoding="utf8").read().splitlines()
        except:
            self.blacklist=[]
        self.base_dm=0
        self.base_login=0
        self.account_path=None
        self.is_licensed=True
        self.is_running=False
        self.ec2_json={}
        self.update_data={
            "bio":None,
            "name":None,
            "user":None,
            "external_url":None,
        }
        try:
            self.data={
                "message":self.message.get("1.0","end-1c"),
                "comment":self.comment.get("1.0","end-1c"),
                "receivers":self.receivers.get("1.0","end-1c"),
                "booleans":[
                    i.get() for i in self.booloeanvars
                ],
                "LoginTiming":int(self.time_each_login.get()) if self.time_each_login.get().isdigit() else 120,
                "BanTiming":int(self.time_each_ban.get()) if self.time_each_ban.get().isdigit() else 300,
                "CycleTiming":int(self.time_each_cycle.get()) if self.time_each_cycle.get().isdigit() else 600,
                "DmTiming":int(self.time_each_dm.get()) if self.time_each_dm.get().isdigit() else 30,
                "FollowTiming":int(self.time_each_follow.get()) if self.time_each_follow.get().isdigit() else 60,
                "LikeTiming":int(self.time_each_like.get()) if self.time_each_like.get().isdigit() else 13,
                "LimitTiming":int(self.time_each_limit.get()) if self.time_each_limit.get().isdigit() else 100,
                "CommentTiming":int(self.time_each_comment.get()) if self.time_each_comment.get().isdigit() else 100,
                "proxies":self.proxy_list,
                "profile_picture":self.picture,
                "publish_post":self.publish_post,
                "publish_story":self.publish_story,
                "update_data":self.update_data,
                "settings":{
                    "timezone":self.timezone,
                    "locale":self.locale_,
                    "country":str(self.locale_).split("_")[-1],
                    "country_code":country.country_prefix(str(self.locale_).split("_")[-1]),
                    "app_version":self.app_version,
                    "model":self.model,
                    "os_version":self.os_version,
                    "scale":self.scale,
                    "resolution":self.resolution,
                    "position":self.position,
                    "timezone":self.timezone,
                    "user_agent":f"Instagram {self.app_version} ({self.model}; {self.os_version}; {self.locale_}; {self.locale_.replace('_','-')}; scale={self.scale}; {self.resolution}; 392223771) {self.position}",
                },
            }
            json.dump(self.data,open(self.base_dir+"data.json","w"),indent=5)
        except:
            self.data={}
        self.main()
    def set_proxy(self,proxy_string:str=None):
        return {"http": f"http://{proxy_string}" if not "://" in proxy_string else proxy_string, "https": f"http://{proxy_string}" if not "://" in proxy_string else proxy_string} if proxy_string is not None else proxy_string

    def exit(self,*args):
        try:
            self.browser.close()
        except:pass
        self.is_running=False
        self.is_closed=True
        try:psutil.Process(os.getpid()).kill()
        except:sys.exit()

    #GUI
    def main(self):
        #root, and geometry
        self.root=Tk()
        self.root.geometry("1200x720")

        #Close command
        self.root.protocol("WM_DELETE_WINDOW",self.exit)

        #Call app builder
        self.build_app()

        self.root.bind("<Control-w>",self.exit)

        #Run
        Thread(target=self.start_license).start()
        self.setTheme()
        self.root.mainloop()

    def start_license(self):
        pass
    def set_icon(self):
        if os.path.exists(self.base_dir+"temp"):
            if os.path.isfile(self.base_dir+"temp"):
                try:
                    self.root.iconbitmap(self.base_dir+"temp")
                    return
                except:
                    pass
        try:
            open(self.base_dir+"temp","wb").write(requests.get("https://automation-it0.github.io/Presentation/GROW-DM.ico").content)
            self.root.iconbitmap(self.base_dir+"temp")
        except:pass
    def settings_window(self):
        self.settings_win=Toplevel(self.root)
        #self.settings_win.geometry(f"{self.root.winfo_width()}x{self.root.winfo_height()}")

        try:self.darkTitleBar(self.settings_win)
        except:pass

        checkbuttonFrame=Frame(self.settings_win)
        checkbuttonFrame.pack(side=TOP,expand=True)
        
        darktheme=BooleanVar(self.settings_win,True)
        androidhttp=BooleanVar(self.settings_win,True)
        webgl=BooleanVar(self.settings_win,False)
        usedll=BooleanVar(self.settings_win,False)
        corerun=BooleanVar(self.settings_win,True)
        debugmode=BooleanVar(self.settings_win,False)
        devgmode=BooleanVar(self.settings_win,False)

        Checkbutton(checkbuttonFrame,text="Dark theme",variable=darktheme).pack(side=TOP,expand=True,anchor="w");
        Checkbutton(checkbuttonFrame,text="Use android http client",variable=androidhttp).pack(side=TOP,expand=True,anchor="w");
        Checkbutton(checkbuttonFrame,text="WebGL",variable=webgl).pack(side=TOP,expand=True,anchor="w");
        Checkbutton(checkbuttonFrame,text="Use windows DLL",variable=usedll).pack(side=TOP,expand=True,anchor="w");
        Checkbutton(checkbuttonFrame,text="Core-Run",variable=corerun).pack(side=TOP,expand=True,anchor="w");
        Checkbutton(checkbuttonFrame,text="Debug mode",variable=debugmode).pack(side=TOP,expand=True,anchor="w");
        Checkbutton(checkbuttonFrame,text="Developer mode",variable=devgmode).pack(side=TOP,expand=True,anchor="w");
        Label(checkbuttonFrame,text="Instagram version").pack(side=TOP,expand=True,anchor="w")
        versionEntry=Entry(checkbuttonFrame);
        versionEntry.pack(side=TOP,expand=True,anchor="w")
        versionEntry.insert(END,self.app_version)

        bottombar=Frame(self.settings_win)
        bottombar.pack(side=BOTTOM,fill=X)
        Button(bottombar,text="Save",command=self.settings_win.destroy,width=10).pack(side=LEFT)
        Button(bottombar,text="Reset",command=self.settings_win.destroy,width=10).pack(side=LEFT)

        self.settings_win.mainloop()
    def build_app(self):
        #Editing root
        self.root.config(background="white")
        self.root.title("GrowDM | Instagram DM Software by GrowPlan.inc 2023 Edition")

        self.toolbar=Frame(self.root)
        self.toolbar.pack(side=TOP,fill=X)
        
        #File export
        self.file_menu = Menu(self.root,tearoff=0)
        self.file_menu.add_command(
            label='Extract user list',
            command=self.extractor
        )
        self.file_menu.add_command(
            label='Filter users on keyword (bio/url)',
            command=self.filterer_keyword
        )
        self.file_menu.add_command(
            label='Clear blacklist',
            command=lambda:open(self.base_dir+"blacklist.txt","w").write("")
        )
        Menubutton(self.toolbar,menu=self.file_menu,text="Tools").pack(side=LEFT)
        Button(self.toolbar,command=self.settings_window,text="Settings").pack(side=LEFT)

        #Modifying icon with thread activity
        icon_thread=Thread(target=self.set_icon)
        icon_thread.start()

        self.root_container=Frame(self.root)
        self.root_container.pack(side=TOP,fill=BOTH,expand=True)

        #Menu at left position
        self.menu_Frame=Frame(self.root_container,width=200)
        self.menu_Frame.pack(fill=Y,side=LEFT,anchor="nw")

        #Frame at right position, console & data container
        self.main_frame=Frame(self.root_container)
        self.main_frame.pack(fill=BOTH,expand=True,side=LEFT)

        #Buttons for menu
        Button(self.menu_Frame,text="Start/Stop",command=self.start).pack(fill=X)
        Button(self.menu_Frame,text="Configure",command=lambda:Thread(target=self.configure).start()).pack(fill=X)

        #Console and data container
        self.console=Text(self.main_frame)
        self.console.pack(side=TOP,expand=True,fill=BOTH)
        self.console.tag_config('warning', background="yellow", foreground="red")
        self.console.tag_config('error', background="red", foreground="black")
        self.console.tag_config('log', background="cyan", foreground="black")
        self.console.tag_config('dm', background="lime", foreground="black")

        self.print("Press on 'Configure' to setup the software")

        self.data_container=Frame(self.main_frame,height="200px")
        self.data_container.pack(side=TOP,fill=X)
        self.banned=Label(self.data_container,font=20,text="Banned:\n0")  # type: ignore
        self.banned.pack(side=LEFT,expand=True,fill=X)
        self.Successful=Label(self.data_container,font=20,text="Successful:\n0")  # type: ignore
        self.Successful.pack(side=LEFT,expand=True,fill=X)
        self.Limited=Label(self.data_container,font=20,text="Limited:\n0")  # type: ignore
        self.Limited.pack(side=LEFT,expand=True,fill=X)
        self.TotalDm=Label(self.data_container,font=20,text="Total DM:\n0")  # type: ignore
        self.TotalDm.pack(side=LEFT,expand=True,fill=X)
        self.Totallogin=Label(self.data_container,font=20,text="Total login:\n0")  # type: ignore
        self.Totallogin.pack(side=LEFT,expand=True,fill=X)
        self.Totalerrors=Label(self.data_container,font=20,text="Total errors:\n0")  # type: ignore
        self.Totalerrors.pack(side=LEFT,expand=True,fill=X)
        self.Blacklisted=Label(self.data_container,font=20,text="Blacklisted:\n0")  # type: ignore
        self.Blacklisted.pack(side=LEFT,expand=True,fill=X)

    def print(self,text:str,type_:str="log",end="\n"):
        try:self.root.geometry()
        except:sys.exit()
        self.console.insert('end', f"{text}{end}", type_)
        self.console.see("end")
        if type_=="error":
            self.add_totalerrors(int(str(self.Totalerrors.cget("text")).split("\n")[-1])+1)
        elif type_=="dm":
            self.add_dm(int(str(self.TotalDm.cget("text")).split("\n")[-1])+1)
        self.log.append(str(text))
        with open(self.logdir+"/Log.txt","a+",encoding="utf8") as log_file:
            log_file.write(f"{type_} - {text}\n")

    def add_banned(self,n:int):
        self.banned.config(text=f"Banned:\n{n}")
    def add_successful(self,n:int):
        self.Successful.config(text=f"Successful:\n{n}")
    def add_limited(self,n:int):
        self.Limited.config(text=f"Limited:\n{n}")
    def add_dm(self,n:int):
        self.TotalDm.config(text=f"Total DM:\n{n}")
    def add_login(self,n:int):
        self.Totallogin.config(text=f"Total login:\n{n}")
    def add_totalerrors(self,n:int):
        self.Totalerrors.config(text=f"Total errors:\n{n}")
    def add_blacklisted(self,n:int):
        self.Blacklisted.config(text=f"Blacklisted:\n{n}")
    def setec2(self):

        def getInput(access:Entry,private:Entry,region:Entry,idbx:Text,scheme:Entry,port:Entry):
            if access.get()=="" or private.get()=="" or port.get()=="" or region.get()=="" or idbx.get("1.0","end-1c")=="":
                messagebox.showwarning("no input given","some data is missing, please insert it and retry!",parent=self.root)
                self.root2.destroy()
                return;
            self.ec2_json.update({
                "access":access.get(),
                "private":private.get(),
                "region":region.get(),
                "port":port.get(),
                "scheme":scheme.get(),
                "id":idbx.get("1.0","end-1c").strip()
            })
            self.root2.destroy()

        self.root2=Toplevel(self.root)

        self.root2.title("EC2 - Set up")

        self.root_uplevel=Frame(self.root2)
        self.root_uplevel.pack(side=TOP)
        self.dFrame=Frame(self.root_uplevel)
        self.rFrame=Frame(self.root_uplevel)
        self.dFrame.pack(side=LEFT,fill=BOTH,expand=1)
        self.rFrame.pack(side=LEFT,fill=BOTH,expand=1)

        Label(self.dFrame,text="AWS Access Key").pack(side=TOP)
        self.access_key_entry=Entry(self.dFrame)
        self.access_key_entry.pack(side=TOP)
        Label(self.dFrame,text="AWS Secret Key").pack(side=TOP)
        self.secret_key_entry=Entry(self.dFrame)
        self.secret_key_entry.pack(side=TOP)
        Label(self.dFrame,text="Region").pack(side=TOP)
        self.region_entry=Entry(self.dFrame)
        self.region_entry.pack(side=TOP)
        Label(self.dFrame,text="Ec2 Port").pack(side=TOP)
        self.port_entry=Entry(self.dFrame)
        self.port_entry.pack(side=TOP)
        Label(self.dFrame,text="Proxy Scheme").pack(side=TOP)
        self.scheme_entry=Entry(self.dFrame)
        self.scheme_entry.pack(side=TOP)
        Label(self.dFrame,text="if you dont know\nwhat a proxy scheme is\ntype \"http\" here...").pack(side=TOP)

        Label(self.rFrame,text="Instance IDs").pack(side=TOP)
        self.idBox=Text(self.rFrame,relief="sunken",bd=2,bg="#171717")
        self.idBox.pack(side=TOP,fill=BOTH,expand=1)

        self.access_key_entry.insert(END,self.ec2_json.get("access",""))
        self.secret_key_entry.insert(END,self.ec2_json.get("private",""))
        self.region_entry.insert(END,self.ec2_json.get("region",""))
        self.scheme_entry.insert(END,self.ec2_json.get("scheme",""))
        self.port_entry.insert(END,self.ec2_json.get("port",""))
        self.idBox.insert(END,self.ec2_json.get("id",""))

        Button(self.root2,text="Save & Continue",command=lambda:getInput(self.access_key_entry,self.secret_key_entry,self.region_entry,self.idBox,self.scheme_entry,self.port_entry)).pack(side=BOTTOM,fill=X)

        self.root2.mainloop()
    def configure(self):

        self.booloeanvars=[
            BooleanVar(self.root,False),#Android
            BooleanVar(self.root,True),#relogin
            BooleanVar(self.root,True),#Story as seen
            BooleanVar(self.root,False),#Like story
            BooleanVar(self.root,False),#Like post
            BooleanVar(self.root,True),#Send message
            BooleanVar(self.root,False),#Send comment
            BooleanVar(self.root,True),#Manually input code
            BooleanVar(self.root,True),#Open browser for login and use sessionID
            BooleanVar(self.root,True),#Download user data
            BooleanVar(self.root,True),#Save account cookies
            BooleanVar(self.root,False),#Save screenshot
            BooleanVar(self.root,True),#Approve login
            BooleanVar(self.root,False),#Close friends
            BooleanVar(self.root,False),#Reply to story as dm
            BooleanVar(self.root,True),#Explore reels after login
            BooleanVar(self.root,True),#Search user before sending
            BooleanVar(self.root,False),#Follow before dm
            BooleanVar(self.root,True),#Random requests
            BooleanVar(self.root,False),#Generate group of 2
            BooleanVar(self.root,False),#Shut down PC
            BooleanVar(self.root,False),#Stop program
            BooleanVar(self.root,False),#No cookies
        ]
        self.configure_window_=Toplevel(self.root)
        self.configure_window_.config(bg="#171717")
        self.configure_window_.config(background="white")

        self.configure_window=Frame(self.configure_window_)
        self.configure_window.pack(side=TOP,expand=True)

        #configure window configuration
        self.configure_window_.protocol("WM_DELETE_WINDOW",self.configure_window_.destroy)
        
        self.configure_window_.title("GrowDM | Configuration Panel")

        self.message_comment_frame=Frame(self.configure_window)
        self.message_comment_frame.pack(side=LEFT,fill=BOTH)

        self.configure_window_.bind("<Control-s>",self.save)

        #Message box
        if 1 == 1:
            Label(self.message_comment_frame,text="Message").pack(side=TOP)

            self.message_inner_frame=Frame(self.message_comment_frame)
            self.message_inner_frame.pack(side=TOP)
            
            self.message=Text(self.message_inner_frame,width=30,height=15,borderwidth=5)
            self.message.pack(side=TOP)

            Button(self.message_comment_frame,text="Load message from txt",command=lambda:self.message.insert(END,open(filedialog.askopenfilename(parent=self.configure_window_),encoding="utf8").read())).pack(side=TOP,fill=X)

        #Comment box
        if 1 == 1:
            Label(self.message_comment_frame,text="Comment").pack(side=TOP)

            self.comment_inner_frame=Frame(self.message_comment_frame)
            self.comment_inner_frame.pack(side=TOP)
            
            self.comment=Text(self.comment_inner_frame,width=30,height=15,borderwidth=5)
            self.comment.pack(side=TOP)
        
            Button(self.message_comment_frame,text="Load comment from txt",command=lambda:self.comment.insert(END,open(filedialog.askopenfilename(parent=self.configure_window_),encoding="utf8").read())).pack(side=TOP,fill=X)

        self.list_settings=Frame(self.configure_window)
        self.list_settings.pack(side=LEFT,fill=BOTH,expand=True)

        #Users box
        if 1 == 1:
            Label(self.list_settings,text="Users").pack(side=TOP)

            self.receiver_inner_frame=Frame(self.list_settings)
            self.receiver_inner_frame.pack(side=TOP)
            
            self.receivers=Text(self.receiver_inner_frame,width=30,height=15,borderwidth=5)
            self.receivers.pack(side=TOP)
        
            Button(self.list_settings,text="Load users from txt",command=lambda:self.receivers.insert(END,open(filedialog.askopenfilename(parent=self.configure_window_),encoding="utf8").read())).pack(side=TOP,fill=X)
        
        #Check boxes
        if 1 == 1:
            Checkbutton(self.list_settings,variable=self.booloeanvars[0],text="Use iPhone instead of Android").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[1],text="Clear cookies if failed login").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[2],text="Mark story as seen").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[3],text="Like first story").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[4],text="Like last post").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[5],text="Send message").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[6],text="Send comment").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[7],text="Manually input code").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[8],text="Open browser to login").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[9],text="Save user data").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[10],text="Save account cookies").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[20],text="Shut down PC after all logins").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[21],text="Stop program after all logins").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.list_settings,variable=self.booloeanvars[22],text="No use of cookies").pack(side=TOP,anchor="w",fill=X)

        self.entry_settings=Frame(self.configure_window)
        self.entry_settings.pack(side=LEFT,fill=BOTH,expand=True)

        #Entry and other check boxes
        if 1 == 1:
            self.entries=Frame(self.entry_settings)
            self.entries.pack(side=LEFT,fill=Y,expand=True)
            Label(self.entries,text="Time after each login").pack(side=TOP,anchor="w",fill=X)
            self.time_each_login=Entry(self.entries)
            self.time_each_login.pack(side=TOP,fill=X)
            Label(self.entries,text="Time after each dm").pack(side=TOP,anchor="w",fill=X)
            self.time_each_dm=Entry(self.entries)
            self.time_each_dm.pack(side=TOP,fill=X)
            Label(self.entries,text="How many dms per account").pack(side=TOP,anchor="w",fill=X)
            self.dms_account=Entry(self.entries)
            self.dms_account.pack(side=TOP,fill=X)
            Label(self.entries,text="Time between each account cycle").pack(side=TOP,anchor="w",fill=X)
            self.time_each_cycle=Entry(self.entries)
            self.time_each_cycle.pack(side=TOP,fill=X)
            Label(self.entries,text="Time after being banned").pack(side=TOP,anchor="w",fill=X)
            self.time_each_ban=Entry(self.entries)
            self.time_each_ban.pack(side=TOP,fill=X)
            Label(self.entries,text="Time after being limited").pack(side=TOP,anchor="w",fill=X)
            self.time_each_limit=Entry(self.entries)
            self.time_each_limit.pack(side=TOP,fill=X)
            Label(self.entries,text="Time after follow").pack(side=TOP,anchor="w",fill=X)
            self.time_each_follow=Entry(self.entries)
            self.time_each_follow.pack(side=TOP,fill=X)
            Label(self.entries,text="Time after comment").pack(side=TOP,anchor="w",fill=X)
            self.time_each_comment=Entry(self.entries)
            self.time_each_comment.pack(side=TOP,fill=X)
            Label(self.entries,text="Time after like").pack(side=TOP,anchor="w",fill=X)
            self.time_each_like=Entry(self.entries)
            self.time_each_like.pack(side=TOP,fill=X)
            Label(self.entries,text="App version").pack(side=TOP,anchor="w",fill=X)
            self.app_version_entry=Entry(self.entries)
            self.app_version_entry.pack(side=TOP,fill=X)

            self.checkboxes_entries=Frame(self.entry_settings)
            self.checkboxes_entries.pack(side=LEFT,fill=Y,expand=True)
            Button(self.checkboxes_entries,command=lambda:self.change("load_accounts"),text="Import Account List").pack(side=TOP,fill=BOTH,expand=True)
            Button(self.checkboxes_entries,command=lambda:self.change("picture"),text="Change profile picture").pack(side=TOP,fill=BOTH,expand=True)
            Button(self.checkboxes_entries,command=lambda:self.change("bio"),text="Change biography").pack(side=TOP,fill=BOTH,expand=True)
            Button(self.checkboxes_entries,command=lambda:self.change("user"),text="Change username").pack(side=TOP,fill=BOTH,expand=True)
            Button(self.checkboxes_entries,command=lambda:self.change("name"),text="Change name").pack(side=TOP,fill=BOTH,expand=True)
            Button(self.checkboxes_entries,command=lambda:self.change("external_url"),text="Change external url").pack(side=TOP,fill=BOTH,expand=True)
            Button(self.checkboxes_entries,command=self.proxy_list_edit,text="Load proxy list").pack(side=TOP,fill=BOTH,expand=True)
            Button(self.checkboxes_entries,command=lambda:self.change("publish_post"),text="Publish post").pack(side=TOP,fill=BOTH,expand=True)
            Button(self.checkboxes_entries,command=lambda:self.change("publish_story"),text="Publish story").pack(side=TOP,fill=BOTH,expand=True)
            Button(self.checkboxes_entries,command=self.setec2,text="Set Up EC2 proxy").pack(side=TOP,fill=BOTH,expand=True)
            Checkbutton(self.checkboxes_entries,variable=self.booloeanvars[11],text="Save screenshot").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.checkboxes_entries,variable=self.booloeanvars[12],text="Approve login").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.checkboxes_entries,variable=self.booloeanvars[13],text="Add user to close friends").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.checkboxes_entries,variable=self.booloeanvars[14],text="Reply to user story as dm").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.checkboxes_entries,variable=self.booloeanvars[15],text="Explore reels after login").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.checkboxes_entries,variable=self.booloeanvars[16],text="Search user before sending").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.checkboxes_entries,variable=self.booloeanvars[17],text="Follow user before DM").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.checkboxes_entries,variable=self.booloeanvars[18],text="Random requests").pack(side=TOP,anchor="w",fill=X)
            Checkbutton(self.checkboxes_entries,variable=self.booloeanvars[19],text="2 People at once").pack(side=TOP,anchor="w",fill=X)
        try:
            self.configure_window_.update() 
        except:pass
        Button(self.configure_window_,text="Confirm and save",command=self.save).pack(side=BOTTOM,fill=X)
        Thread(target=self.load_data).start()

    def load_data(self):
        if os.path.exists(self.base_dir+"data.json"):
            try:
                data=dict(**json.load(open(self.base_dir+"data.json")))
                self.message.insert(END,data.get("message",""))
                self.comment.insert(END,data.get("comment",""))
                self.receivers.insert(END,"\n".join(data.get("receivers","")))
                for boolean,value in zip(self.booloeanvars,data["booleans"]):
                    try:
                        boolean.set(value==True)
                    except:pass
                self.time_each_login.insert(END,data.get("LoginTiming","0"))
                self.time_each_ban.insert(END,data.get("BanTiming","0"))
                self.time_each_cycle.insert(END,data.get("CycleTiming","0"))
                self.time_each_dm.insert(END,data.get("DmTiming","0"))
                self.time_each_follow.insert(END,data.get("FollowTiming","0"))
                self.time_each_like.insert(END,data.get("LikeTiming","0"))
                self.time_each_limit.insert(END,data.get("LimitTiming","0"))
                self.time_each_comment.insert(END,data.get("CommentTiming","0"))
                self.dms_account.insert(END,data.get("DmsAccount","10"))
                self.ec2_json=data.get("ec2",{})
                self.proxy_list=data.get("proxylist",[])
                self.picture=data.get("profile_picture",[])
                self.publish_post=data.get("publish_post",[])
                self.publish_story=data.get("publish_story",[])
                self.update_data=data.get("update_data",{
                    "bio":None,
                    "user":None,
                    "username":None,
                    "external_url":None
                })
                self.account_path=data.get("account_path",None)
            except:
                print(traceback.format_exc())
    def proxy_list_edit(self):
        path_=filedialog.askopenfilename(parent=self.configure_window,filetypes=[("text file",".txt"),("all files","*.*")])
        if path_=="":return
        self.proxy_list=open(path_).read().splitlines()
        self.print("setted proxies")
    
    def change(self,type_:str):
        if type_ not in ["picture","bio","user","name","external_url","publish_post","publish_story","load_accounts"]:return
        if type_=="picture":
            path_=filedialog.askopenfilename(parent=self.configure_window,filetypes=[("Jpg image",".jpg")])
            if path_=="":return
            self.picture.append(path_)
        elif type_ in ["bio","user","name","external_url"]:
            box=simpledialog.askstring("",prompt=f"Insert value for {type_}")
            if box is None or box=="":return
            self.update_data.update(
                {
                    "type_":box  # type: ignore
                }
            )
        elif type_ == "publish_post":
            path_=filedialog.askopenfilename(parent=self.configure_window,filetypes=[("Jpg image",".jpg")])
            if path_=="":return
            self.publish_post.append(path_)
        elif type_ == "load_accounts":
            path_=filedialog.askopenfilename(parent=self.configure_window,filetypes=[("Excel Spreadsheet",".xlsx"),("Excel Spreadsheet",".xls"),("Libreoffice calc file",".ods"),("Text file",".txt"),("CSV File",".csv",)])
            if path_=="":return
            self.account_path=path_
        elif type_ == "publish_story":
            path_=filedialog.askopenfilename(parent=self.configure_window,filetypes=[("Jpg image",".jpg")])
            if path_=="":return
            self.publish_story.append(path_)
        else:
            messagebox.showwarning(message="Option not avaiable now.",parent=self.configure_window)
    def save(self,*args):
        try:
            self.app_version=self.app_version_entry.get() if self.app_version_entry.get()!="" else self.app_version
            self.data={
                "message":self.message.get("1.0","end-1c"),
                "comment":self.comment.get("1.0","end-1c"),
                "receivers":self.receivers.get("1.0","end-1c").splitlines(),
                "booleans":[
                    i.get() for i in self.booloeanvars
                ],
                "LoginTiming":int(self.time_each_login.get()) if self.time_each_login.get().isdigit() else 120,
                "BanTiming":int(self.time_each_ban.get()) if self.time_each_ban.get().isdigit() else 300,
                "CycleTiming":int(self.time_each_cycle.get()) if self.time_each_cycle.get().isdigit() else 600,
                "DmTiming":int(self.time_each_dm.get()) if self.time_each_dm.get().isdigit() else 30,
                "FollowTiming":int(self.time_each_follow.get()) if self.time_each_follow.get().isdigit() else 60,
                "LikeTiming":int(self.time_each_like.get()) if self.time_each_like.get().isdigit() else 13,
                "LimitTiming":int(self.time_each_limit.get()) if self.time_each_limit.get().isdigit() else 100,
                "CommentTiming":int(self.time_each_comment.get()) if self.time_each_comment.get().isdigit() else 100,
                "DmsAccount":int(self.dms_account.get()) if self.dms_account.get().isdigit() else 100,
                "proxies":self.proxy_list,
                "profile_picture":self.picture,
                "publish_post":self.publish_post,
                "publish_story":self.publish_story,
                "update_data":self.update_data,
                "account_path":self.account_path,
                "ec2":self.ec2_json,
                "settings":{
                    "timezone":self.timezone,
                    "locale":self.locale_,
                    "country":str(self.locale_).split("_")[-1],
                    "country_code":country.country_prefix(str(self.locale_).split("_")[-1]),
                    "app_version":self.app_version,
                    "model":self.model,
                    "os_version":self.os_version,
                    "scale":self.scale,
                    "resolution":self.resolution,
                    "position":self.position,
                    "user_agent":f"Instagram {self.app_version} ({self.model}; {self.os_version}; {self.locale_}; {self.locale_.replace('_','-')}; scale={self.scale}; {self.resolution}; 392223771) {self.position}",
                },
            }
            json.dump(self.data,open(self.base_dir+"data.json","w"),indent=5)
        except:pass
        self.configure_window_.destroy()
    def settings(self):pass
    def help(self):pass
    def tips(self):pass


    def start(self):
        self.is_running=not self.is_running
        if self.is_running:
            self.print("starting thread")
            self.start_thread=Thread(target=self.thread_)
            self.start_thread.start()
        else:
            self._count = 0;
            self.print("thread is shutting down")
            self.root.after(2500,self.onForever)
    def onForever(self,*args,**kwargs):
        if self.start_thread.is_alive():
            self.print("thread has not shut down yet, waiting 2.5 seconds...")
            self._count+=1
            if self._count<7:
                self.root.after(2500,self.onForever)
            else:
                self._count=0
        else:
            self.print("thread has successfully shut down")
    def manual_input_code(self, username: str, choice=None):
        try:
            temp_root=Tk()
            temp_root.withdraw()
            code=simpledialog.askstring("",prompt=f"Type code for {username}, type: {choice}",parent=temp_root)
            if code is None or (not code.isdigit()):
                code=str(random__())
            temp_root.destroy()
            return code
        except Exception as e:
            return str(random__())
    def screenshot(self,account:str,path_to_save:str,user:str,message:str,nDM:int,n2:int):
        pass
    def thread_(self):
        try:
            if self.data=={}:
                if not os.path.exists(self.base_dir+"data.json"):
                    self.print("No configuration file found, try setting it again!","warning")
                else:
                    self.data=dict(**json.load(open(self.base_dir+"data.json",encoding="utf8")))
            self.settings_=Settings(
                self.data.get("DmsAccount",15),
                self.data["account_path"],
                self.data["message"],
                self.data["comment"],
                self.data["receivers"],
                self.data["LoginTiming"],
                self.data["BanTiming"],
                self.data["CycleTiming"],
                self.data["DmTiming"],
                self.data["FollowTiming"],
                self.data["LikeTiming"],
                self.data["LimitTiming"],
                self.data["CommentTiming"],
                self.data["proxies"],
                self.data["profile_picture"],
                self.data["publish_post"],
                self.data["publish_story"],
                self.data["update_data"],
                self.data["settings"]["timezone"],
                self.data["settings"]["locale"],
                self.data["settings"]["country"],
                self.data["settings"]["country_code"],
                self.data["settings"]["app_version"],
                self.data["settings"]["model"],
                self.data["settings"]["os_version"],
                self.data["settings"]["scale"],
                self.data["settings"]["resolution"],
                self.data["settings"]["position"],
                self.data["settings"]["user_agent"],
                *self.data["booleans"]
            )
            if self.settings_.saveScreenshot:
                try:
                    options=ChromeOptions()
                    options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
                    options.add_experimental_option("excludeSwitches", ["enable-logging"])
                    options.headless=True
                    options.add_argument('--no-sandbox')
                    options.add_argument('--headless')
                    options.add_argument('--disable-gpu')
                    self.browser=Chrome(executable_path=ChromeDriverManager().install(),options=options)
                    self.browser.set_window_size(390,850)
                    self.print("Browser initialized")
                except Exception as e:
                    self.print(e)
            if self.settings_.accountPath is None or not os.path.exists(self.settings_.accountPath):
                self.print("Speficy accounts to use! program stopped","error")
                self.is_running=False
                return
            if len(self.settings_.receivers)<1:
                self.print("User list is not long enough, specifiy a user list longer than 0 users then retry","error")
                self.is_running=False
                return
            if self.settings_.message=="":
                self.print("Message cannot be empty, setup message again and retry","error")
                self.is_running=False
                return
            settings={
                    "device_settings": 
                    {
                        "app_version": f"{self.settings_.app_version}",
                        "android_version": 33,
                        "android_release": "13.0.0",
                        "dpi": "560dpi",
                        "resolution": "1440x2934",
                        "manufacturer": "Google/google",
                        "device": "raven",
                        "model": "Pixel 6",
                        "cpu": "raven",
                        "version_code": "314665256"
                    },
                    "timezone":self.timezone,
                    "locale":self.locale_,
                    "country":str(self.locale_).split("_")[-1],
                    "country_code":country.country_prefix(str(self.locale_).split("_")[-1])
                }
            settings={} # remove to keep old settings
            self.client=Client(
                settings=settings
            )

            if self.settings_.inputCode:
                self.client.challenge_code_handler=self.manual_input_code
            else:
                self.client.challenge_code_handler=random__
            self.account_path=self.settings_.accountPath
            ec2_stanced=False
            if self.ec2_json!={}:
                try:
                    self.fullstances=[]
                    self.print(f"""Loading AWS instance in region {self.ec2_json.get("region",'us-west-1')}""")
                    conn=boto3.client('ec2', aws_access_key_id=self.ec2_json.get("access"), aws_secret_access_key=self.ec2_json.get("private"),region_name=self.ec2_json.get("region",'us-west-1'))
                    rsc=boto3.resource('ec2', aws_access_key_id=self.ec2_json.get("access"), aws_secret_access_key=self.ec2_json.get("private"),region_name=self.ec2_json.get("region",'us-west-1'))
                    instances = get_stopped_instances(conn)
                    self.print(f"""Loaded successfully, checking avaiable (stopped) instances...""")
                    for instance in instances:
                        if instance in self.ec2_json.get("id",""):
                            self.fullstances.append(instance)
                            self.print(f"Found instance: {instance}")
                        else:
                            self.print(f"Instance {instance} is not present in user input, skipping")
                    ec2_stanced=True
                except Exception as e:
                    self.print(f"could not load ec2 client, error message {e}","error")
            try:
                if ".xlsx" in self.account_path or ".ods" in self.account_path:
                    self.accounts=read_excel(self.account_path)
                    self.print("loading users with excel file")
                    if self.accounts.get("Username",None) is None:
                        self.print("On excel and csv file specify 'Username' and 'Password' column, retry","error")
                        return
                elif ".csv" in self.account_path:
                    self.accounts=read_csv(self.account_path)
                    self.print("loading users with csv")
                    if self.accounts.get("Username",None) is None:
                        self.print("On excel and csv file specify 'Username' and 'Password' column, retry","error")
                        return
                elif ".txt" in self.account_path:
                    user_=open(self.account_path,encoding="utf8").read().splitlines()
                    if ":" in user_[0] and "|" in user_[0] and("=" in user_[0] or "{" in user_[0]):
                        self.print("loading users with ':' separator and cookies separated with |")
                        self.accounts={
                            "Username":[i.split(":")[0] for i in user_],
                            "Password":[i.split(":",1)[1].split("|",1)[0] for i in user_],
                            "other":[i.split(":",1)[1].split("|",1)[1] for i in user_],
                        }
                    elif ":" in user_[0]:
                        self.print("loading users with ':' separator")
                        self.accounts={
                            "Username":[i.split(":")[0] for i in user_],
                            "Password":[i.split(":")[1] for i in user_],
                            "other":range(len(user_))
                        }
                    elif "," in user_[0]:
                        self.print("loading users with ',' separator")
                        self.accounts={
                            "Username":[i.split(",")[0] for i in user_],
                            "Password":[i.split(",")[1] for i in user_],
                            "other":range(len(user_))
                        }
                    elif ";" in user_[0]:
                        self.print("loading users with ';' separator")
                        self.accounts={
                            "Username":[i.split(";")[0] for i in user_],
                            "Password":[i.split(";")[1] for i in user_],
                            "other":range(len(user_))
                        }
                    else:
                        self.print("Separator not detected, retry","error")
                        return
            except Exception as e:
                self.print(f"Cannot load user list {e}, retry","error")
                return
            if not self.is_running:
                return
            self.is_first_login=True
            if not os.path.exists(f"{self.base_dir}blacklist.txt"):
                open(f"{self.base_dir}blacklist.txt","w").close()
            else:
                self.blacklist=open(f"{self.base_dir}blacklist.txt").read().splitlines()
            self.user_to_share=None
            self.media_to_share=None
            self.index_ec2=0
            while True:
                for user,password in zip(self.accounts["Username"],self.accounts["Password"]):
                    self.client=Client()
                    if not self.is_running:return;
                    works=False
                    while not works and ec2_stanced:
                        try:
                            if self.ec2_json!={}:
                                status_=stop_instances(conn,self.fullstances)
                            else:break;
                        except Exception as e:
                            pass
                        try:
                            if self.ec2_json!={}:
                                ip_=start_instance(conn,rsc,self.fullstances[self.index_ec2])
                                for i in range(3):
                                    time.sleep(25)
                                    ip_=get_instance_public_ip_(conn,self.fullstances[self.index_ec2])
                                    for r in range(5):
                                        ip_=get_instance_public_ip_(conn,self.fullstances[self.index_ec2])
                                        try:
                                            resp=requests.get("https://www.google.com",proxies={
                                                "http":f"{self.ec2_json.get('scheme','http')}://{ip_}:{self.ec2_json.get('port','3124')}",
                                                "https":f"{self.ec2_json.get('scheme','http')}://{ip_}:{self.ec2_json.get('port','3124')}",
                                            })
                                            works=True
                                            self.print(f"IP {ip_} works!!! response from google.com:{resp.status_code}")
                                            break;
                                        except:
                                            self.print(f"IP {ip_} is still not working...","warning")
                                            time.sleep(20)
                                    else:
                                        self.print("proxy was not able to work after being tested 5 times...")
                                    self.last_proxy=f"{self.ec2_json.get('scheme','http')}://{ip_}:{self.ec2_json.get('port','3124')}"
                                    self.client.set_proxy(self.last_proxy)
                                    self.print(f"Loaded proxy {self.last_proxy} successfully")
                                    break;
                                self.print(f"started ec2 {self.fullstances[self.index_ec2]}")
                                self.index_ec2+=1
                                if self.index_ec2==len(self.fullstances):
                                    self.index_ec2=0
                            else:break;
                        except IndexError:
                            self.index_ec2=0
                        except Exception as e:
                            self.index_ec2+=1
                    if not self.is_running:return;
                    try:
                        if len(self.settings_.proxies)>0:
                            self.last_proxy=random.choice(self.settings_.proxies)
                            if self.last_proxy!=None:
                                self.client.set_proxy(self.last_proxy)
                                self.print(f"Loaded proxy {self.last_proxy} successfully")
                    except:
                        self.print(f"Cannot load proxy {self.last_proxy}","warning")
                    if not self.is_first_login:
                        time.sleep(int(self.settings_.loginTiming))
                    else:
                        self.is_first_login=False
                    if not self.is_running:return;
                    self.print(f"Logging in as {user}, IG version: {self.settings_.app_version}")
                    failed=False
                    try:
                        self.add_login(int(str(self.Totallogin.cget("text")).split("\n")[-1])+1)
                        if not self.settings_.noCookies:
                            try:
                                pass
                                #self.client.load_settings(self.base_dir+f"{user}.json")
                            except:pass
                        self.last_login=self.login(user,password)
                        try:
                            if self.settings_.saveCookies:
                                self.client.dump_settings(self.base_dir+f"{user}.json")
                        except:pass
                    except Exception as e:
                        self.last_login=str(e)
                        failed=True
                    if self.last_login=="Challenge":
                        open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;CHALLENGE_OBJECT<Enum 660-900>\n")
                        self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        self.print(f"Failed to login as {user}, Account is banned or challenge-required!","error")
                        continue
                    elif self.last_login=="BadPassword":
                        try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;BAD_KEY_OR_PASSWORD<ClientObject 5-7>\n")
                        except:pass
                        self.print(f"Failed to login as {user}, Password {password} is wrong!","warning")
                        continue
                    elif self.last_login=="RateLimit":
                        try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;HTTP_403_POINTER<HttpService.dll 128-565>\n")
                        except:pass
                        self.print(f"Failed to login as {user}, IP address is Rate Limited!","warning")
                        continue
                    elif failed:
                        try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;REFUSED_CODE<ClientObject 1156-1296>\n")
                        except:pass
                        self.print(f"Failed to login as {user}, error code {self.last_login}","warning")
                        continue
                    elif self.last_login=="Checkpoint":
                        try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;REFUSED_CODE<ClientObject 1156-1296>\n")
                        except:pass
                        self.print(f"Failed to login as {user}, checkpoint required","error")
                        continue
                    if not self.is_running:return;

                    else:
                        try:
                            open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;ACCEPTED_KEY_VALID_LOGIN<ClientObject 390-403>\n")
                        except:pass
                        try:
                            if self.client.new_feed_exist():
                                self.client.news_inbox_v1()
                                self.client.get_timeline_feed()
                            try:
                                open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};NOTIFICATION;SUCCESS\n")
                            except:pass
                            if (self.user_to_share is None or self.media_to_share is None) and "[https://www.instagram.com/" in self.settings_.message:
                                if("[https://www.instagram.com/p/" in self.settings_.message):
                                    try:
                                        temp_media="".join([i for i in self.settings_.message.split("[",1)[1].split("]",1)[0] if ("/p/" in self.settings_.message)])
                                        self.media_to_share=self.client.media_info(self.client.media_pk_from_url(temp_media)).id
                                        self.settings_.message=self.settings_.message.replace("["+temp_media+"]","")
                                        self.client.media_seen(self.media_to_share)
                                    except:pass
                                else:
                                    try:
                                        user_temp="".join([i for i in self.settings_.message.split("[",1)[1].split("]",1)[0].split("/",3)[-1].replace("/","") if ("/p/" not in self.settings_.message)])
                                        self.user_to_share=self.client.user_info_by_username_v1(user_temp).pk
                                        self.settings_.message=self.settings_.message.replace(
                                            "[https://www.instagram.com/"+user_temp+"]",""
                                            )
                                        self.settings_.message=self.settings_.message.replace(
                                            "[https://www.instagram.com/"+user_temp+"/]",""
                                            )
                                    except:pass
                                try:
                                    open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};PARSE_MEDIA_MESSAGE;SUCCESS\n")
                                except:pass
                        except exceptions.LoginRequired:
                            self.print(f"Failed execute action as {user}, account has been logged out","warning")
                            continue
                        except exceptions.ChallengeRequired:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeSelfieCaptcha:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeUnknownStep:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except Exception as e:
                            self.print(f"Failed execute action as {user}.\nlast response:{self.client.last_json}, error type {e}, continuing","warning")
                        
                        try:
                            if not self.is_running:return;
                            if self.settings_.updateData.get("bio",None)is None or self.settings_.updateData.get("name",None)is None or self.settings_.updateData.get("user",None)is None or self.settings_.updateData.get("external_url",None)is None:
                                try:
                                    user_data = self.client.account_info().dict()
                                    self.client.account_edit(user_data.update(
                                        {
                                            "biography":self.settings_.updateData.get("bio",None) if self.settings_.updateData.get("bio",None) is not None else user_data.get("biography",None),
                                            "full_name":self.settings_.updateData.get("name",None) if self.settings_.updateData.get("name",None) is not None else user_data.get("full_name",None),
                                            "username":self.settings_.updateData.get("user",None) if self.settings_.updateData.get("user",None) is not None else user_data.get("username",None),
                                            "external_url":self.settings_.updateData.get("external_url",None) if self.settings_.updateData.get("external_url",None) is not None else user_data.get("external_url",None),
                                        }
                                    ))
                                    open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};UPDATE_ACCOUNT_DATA;SUCCESS\n")
                                except:pass
                        except exceptions.LoginRequired:
                            self.print(f"Failed execute action as {user}, account has been logged out","warning")
                        except exceptions.ChallengeRequired:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeSelfieCaptcha:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeUnknownStep:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except:
                            self.print(f"Failed to update profile data as {user}.\nlast response:{self.client.last_json}, continuing","warning")
                        
                        try:
                            if len(self.settings_.profile)>0:
                                self.client.account_change_picture(random.choice(self.settings_.profile))
                                try:
                                    open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};UPDATE_ACCOUNT_IMAGE;SUCCESS\n")
                                except:pass
                        except exceptions.LoginRequired:
                            self.print(f"Failed execute action as {user}, account has been logged out","warning")
                        except exceptions.ChallengeRequired:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeSelfieCaptcha:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeUnknownStep:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except:
                            self.print(f"Failed to change profile picture as {user}.\nlast response:{self.client.last_json}, continuing","warning")
                        
                        try:
                            if self.settings_.exploreReels:
                                self.client.explore_reels(10)
                                try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};REEL_EXPLORE;SUCCESS\n")
                                except:pass
                        except exceptions.LoginRequired:
                            self.print(f"Failed execute action as {user}, account has been logged out","warning")
                        except exceptions.ChallengeRequired:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeSelfieCaptcha:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeUnknownStep:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except Exception as e:
                            self.print(f"Failed to explore reels as {user}.\nlast response:{self.client.last_json}, error type {e}, continuing","warning")
                        
                        try:
                            if len(self.settings_.post)>0:
                                try:
                                    self.client.photo_upload(random.choice(self.settings_.post))
                                    time.sleep(30)
                                    open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};PHOTO_UPLOAD;SUCCESS\n")
                                except:pass
                            if len(self.settings_.story)>0:
                                try:
                                    self.client.photo_upload_to_story(random.choice(self.settings_.story))
                                    time.sleep(30)
                                    open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};STORY_PHOTO_UPLOAD;SUCCESS\n")
                                except:pass
                            
                            self.print(f"Successfully logged in","log")
                            self.add_successful(int(str(self.Successful.cget("text")).split("\n")[-1])+1)
                            self.print(f"Successfully loaded feed","log")
                        except exceptions.LoginRequired:
                            self.print(f"Failed execute action as {user}, account has been logged out","warning")
                            continue
                        except exceptions.ChallengeRequired:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeSelfieCaptcha:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except exceptions.ChallengeUnknownStep:
                            self.print(f"Failed execute action as {user}, Account is banned!","error")
                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                        except:
                            self.print(f"Failed upload media as {user}.\nlast response:{self.client.last_json}, continuing","warning")
                        
                        if not self.is_running:return;
                        for n_dm in range(self.settings_.DmsAccount):
                            if not self.is_running:return;
                            try:
                                if len(self.settings_.receivers)<1:
                                    self.print(f"Receiver list finished, exiting","log")
                                    self.is_running=not self.is_running
                                    sys.exit()
                                while True:
                                    if len(self.settings_.receivers)<1:
                                        self.print(f"Receiver list finished, exiting","log")
                                        self.is_running=not self.is_running
                                        sys.exit()
                                    self.last_receiver=self.settings_.receivers.pop(0)
                                    if self.last_receiver not in self.blacklist:
                                        self.blacklist.append(self.last_receiver)
                                        try:
                                            open(f"{self.base_dir}blacklist.txt","a+").write(self.last_receiver+"\n")
                                        except:
                                            pass
                                        break
                                    else:
                                        self.print(f"User - {self.last_receiver} already received a message")
                                        self.add_blacklisted(int(str(self.Blacklisted.cget("text")).split("\n")[-1])+1)
                                
                                self.user_object=(self.client.user_info(self.last_receiver) if self.last_receiver.isdigit() else 
                                        self.client.user_info(self.client.search_users(self.last_receiver)[0].pk)) if self.settings_.searchBeforeDm else self.client.user_info_by_username_v1(self.last_receiver)
                                try:
                                    open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOAD_USER_LAZY;SUCCESS\n")
                                except:pass
                                
                                self.last_receiver=self.user_object.username
                                self.user_medias=self.client.user_medias(self.user_object.pk,9)
                                
                                try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOAD_MEDIA_LAZY;SUCCESS\n")
                                except:pass
                                self.story=self.client.user_stories(self.user_object.pk)
                                try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOAD_STORY_LAZY;SUCCESS\n")
                                except:pass
                                
                                if self.settings_.storyAsSeen:
                                    try:
                                        self.client.story_seen([i.pk for i in self.story])
                                        if self.settings_.likeStory:
                                            self.client.story_like(self.story[0].id)
                                        self.sleep(10)
                                        try:
                                            open(self.storyview_log,"a+").write(f"{self.client.username};{datetime.datetime.now().strftime('%T %D')};{n_dm};{self.last_receiver}\n")
                                            open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};STORY_POST_ACTION;SUCCESS\n")
                                        except:pass
                                    except:
                                        try:
                                            open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};STORY_POST_ACTION;BADRESPONSE\n")
                                        except:pass
                                if self.settings_.downloadUser:
                                    try:
                                        self.user_object=self.client.user_info(self.user_object.pk)
                                        if not os.path.exists("User-downloaded.csv"):
                                            open("User-downloaded.csv","w",encoding="utf8").write("sep=;\nUsername;Name;Followers;Followings;Posts;Email;Phone;Verified;Business;Biography;Url")
                                        open("User-downloaded.csv","a+",encoding="utf8").write(f"{self.user_object.username};{self.user_object.full_name};{self.user_object.follower_count};{self.user_object.following_count};{self.user_object.media_count};{self.user_object.public_email};{self.user_object.public_phone_country_code}-{self.user_object.public_phone_number};{self.user_object.is_verified};{self.user_object.is_business};"+str(self.user_object.biography).replace("\n","")+f";{self.user_object.external_url}\n")
                                        open("User-downloaded.txt","a+",encoding="utf8").write(f"{self.user_object.username};{self.user_object.full_name};{self.user_object.follower_count};{self.user_object.following_count};{self.user_object.media_count};{self.user_object.public_email};{self.user_object.public_phone_country_code}-{self.user_object.public_phone_number};{self.user_object.is_verified};{self.user_object.is_business};{self.user_object.external_url}\n")
                                        open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};SAVE_USER;SUCCESS\n")
                                    except:
                                        try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};SAVE_USER;BADRESPONSE\n")
                                        except:pass
                                
                                if self.settings_.followBeforeDm:
                                    try:
                                        self.client.user_follow(self.user_object.pk)
                                        self.print("User followed")
                                        try:
                                            d_=datetime.datetime.now()
                                            open(self.base_dir+"followed-log.txt","a+").write("time %3dd/%3dm/%5dy %3dh:%3dm:%3ds; to %20s; using %20s\n" % d_.day,d_.month,d_.year,d_.hour,d_.minute,d_.second,"".join(self.last_receiver),user)
                                            open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};FOLLOW;SUCCESS\n")
                                        except:pass
                                        self.sleep(self.settings_.followTiming)
                                    except:
                                        try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};FOLLOW;BADRESPONSE\n")
                                        except:pass
                                
                                if self.settings_.likePost:
                                    if len(self.user_medias)>0:
                                        try:
                                            self.client.media_like(self.user_medias[0].id)
                                            try:
                                                d_=datetime.datetime.now()
                                                open(self.base_dir+"like-log.txt","a+").write("time %3dd/%3dm/%5dy %3dh:%3dm:%3ds; to %20s; using %20s\n" % d_.day,d_.month,d_.year,d_.hour,d_.minute,d_.second,"".join(self.last_receiver),user)
                                            except:pass
                                            try:
                                                open(self.like_log,"a+").write(f"{self.client.username};{datetime.datetime.now().strftime('%T %D')};{n_dm};https://www.instagram.com/p/{self.user_medias[0].code}\n")
                                                open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LIKE_POST_ACTION;SUCCESS\n")
                                            except:pass
                                            self.sleep(self.settings_.likeTiming)
                                        except:
                                            try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LIKE_POST_ACTION;BADRESPONSE\n")
                                            except:pass
                                if self.settings_.closeFriends:
                                    try:
                                        self.client.close_friend_add(self.user_object.pk)
                                        try:
                                            d_=datetime.datetime.now()
                                            open(self.base_dir+"closefriends-log.txt","a+").write("time %3dd/%3dm/%5dy %3dh:%3dm:%3ds; to %20s; using %20s\n" % d_.day,d_.month,d_.year,d_.hour,d_.minute,d_.second,"".join(self.last_receiver),user)
                                            open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};FRIEND_ADD_POST_ACTION;SUCCESS\n")
                                        except:pass
                                        self.print(f"user {self.last_receiver} added to close friends of {user}","log")
                                    except:
                                        try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};FRIEND_ADD_POST_ACTION;BADRESPONSE\n")
                                        except:pass
                                if self.settings_.sendComment:
                                    if len(self.user_medias)>0:
                                        try:
                                            self.client.media_comment(self.user_medias[0].id,self.settings_.comment.replace("{receiver}",self.user_object.username).replace("{name}",self.user_object.full_name))
                                            try:
                                                d_=datetime.datetime.now()
                                                open(self.base_dir+"comment-log.txt","a+").write("time %3dd/%3dm/%5dy %3dh:%3dm:%3ds; to %20s; using %20s\n" % d_.day,d_.month,d_.year,d_.hour,d_.minute,d_.second,"".join(self.last_receiver),user)
                                            except:pass
                                            try:
                                                open(self.comment_log,"a+").write(f"{self.client.username};{datetime.datetime.now().strftime('%T %D')};{n_dm};instagram.com/p/{self.user_medias[0].code}\n")
                                                open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};COMMENT_POST_ACTION;SUCCESS\n")
                                            except:pass
                                            self.print(f"Comment n{n_dm} sent to {self.last_receiver} using {user}","dm")
                                            self.sleep(self.settings_.commentTiming)
                                        except Exception as e:
                                            try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};COMMENT_POST_ACTION;BADRESPONSE\n")
                                            except:pass
                                            if not self.settings_.sendMessage:
                                                raise e
                                if self.settings_.sendMessage:
                                    try:
                                        if self.settings_.replyStoryAsDm:
                                            try:
                                                self.client.direct_story_share(self.story[0].id)
                                                open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};DIRECT_STORY_SHARE;SUCCESS\n")
                                            except:
                                                try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};DIRECT_STORY_SHARE;BADRESPONSE\n")
                                                except:pass
                                        if self.user_to_share is not None:
                                            try:
                                                self.client.direct_profile_share(self.user_to_share,[self.user_object.pk])
                                                try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};DIRECT_PROFILE_SHARE;SUCCESS\n")
                                                except:pass
                                            except:
                                                try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};DIRECT_PROFILE_SHARE;BADRESPONSE\n")
                                                except:pass
                                        self.last_users=[self.user_object.pk]
                                        self.last_users_name=[self.user_object.username]
                                        if self.settings_.createGroup:
                                            while True:
                                                if len(self.settings_.receivers)<1:
                                                    self.print(f"Receiver list finished, exiting","log")
                                                    try:
                                                        self.browser.close()
                                                    except:pass
                                                    break
                                                self.last_receiver=self.settings_.receivers.pop(0)
                                                if self.last_receiver not in self.blacklist:
                                                    self.blacklist.append(self.last_receiver)
                                                    try:
                                                        open(f"{self.base_dir}blacklist.txt","a+").write(self.last_receiver+"\n")
                                                    except:
                                                        pass
                                                    break
                                                else:
                                                    self.print(f"User - {self.last_receiver} already received a message")
                                                    self.add_blacklisted(int(str(self.Blacklisted.cget("text")).split("\n")[-1])+1)
                                            self.next_user_object=self.client.user_info_v1(
                                                self.last_receiver if self.last_receiver.isdigit() else 
                                                    self.client.search_users(self.last_receiver)[0].pk) if self.settings_.searchBeforeDm else self.client.user_info_by_username_v1(self.last_receiver)
                                            self.last_users.append(self.next_user_object.pk)
                                            self.last_users_name.append(self.next_user_object.username)
                                            try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};DIRECT_GROUP_FORM;SUCCESS\n")
                                            except:pass
                                        try:
                                            self.client.direct_send(self.settings_.message.replace("{receiver}",self.user_object.username).replace("{name}",self.user_object.full_name),self.last_users)
                                        except Exception as e:
                                            self.sleep(round(random.uniform(3,5),2))
                                            self.client.direct_send(self.settings_.message.replace("{receiver}",self.user_object.username).replace("{name}",self.user_object.full_name),self.last_users)
                                        self.print(f"DM n{n_dm} sent to {self.last_receiver} using {user}","dm")
                                        try:
                                            open(self.dm_log,"a+").write(f"{self.client.username};{datetime.datetime.now().strftime('%T %D')};{n_dm};{' '.join(self.last_users_name)};{' '.join(self.last_users)}\n")
                                            open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};DIRECT_SEND;SUCCESS\n")
                                        except:pass
                                        try:
                                            d_=datetime.datetime.now()
                                            open(self.base_dir+"dm-log.txt","a+").write("time %3dd/%3dm/%5dy %3dh:%3dm:%3ds; to %20s; using %20s\n" % d_.day,d_.month,d_.year,d_.hour,d_.minute,d_.second,"".join(self.last_users_name),user)
                                        except:pass
                                        self.screenshot(self.client.username,"screenshot/"," And ".join(self.last_users_name),self.settings_.message,n_dm,int(str(self.TotalDm.cget("text")).split("\n")[-1])+1)
                                        self.sleep(self.settings_.dmTiming)
                                    except Exception as e:
                                        try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};DIRECT_SEND;BADRESPONSE\n")
                                        except:pass
                                        raise e
                                self.add_dm(int(str(self.TotalDm.cget("text")).split("\n")[-1])+1)
                            except exceptions.ChallengeRequired:
                                self.print(f"Failed to send message to {self.last_receiver}, Account is banned!","error")
                                self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                                break
                            except exceptions.ChallengeSelfieCaptcha:
                                self.print(f"Failed to send message to {self.last_receiver}, Account is banned!","error")
                                self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                                break
                            except exceptions.ChallengeUnknownStep:
                                self.print(f"Failed to send message to {self.last_receiver}, Account is banned!","error")
                                self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                                break
                            except exceptions.UserNotFound:
                                try:
                                    open(self.users_not_found_log,"a+").write(f"{self.client.username};{datetime.datetime.now().strftime('%T %D')};{n_dm};{' '.join(self.last_users_name)};{' '.join(self.last_users)}\n")
                                except:pass
                                self.print(f"Failed to send message to {self.last_receiver}, User not found!","warning")
                                self.add_blacklisted(self.last_receiver) 
                            except IndexError:
                                print("idx")
                            except Exception as e:
                                self.print(f"Limited while sending dm/comment {e}","error")
                                try:
                                    if self.client.last_json.get("status_code","200")=="403":
                                        self.print(f"403 status code, IP might be limited!","warning")
                                    """ elif "login_required" in str(e).lower():
                                        try:
                                            self.client.logout()
                                        except:
                                            pass
                                        try:
                                            self.client.init()
                                            self.client.authorization_data={}
                                            self.client.private.headers.update({'Authorization': self.client.authorization})
                                            self.last_login=self.login(user,password)
                                        except Exception as e:
                                            self.last_login=str(e)
                                            failed=True
                                        if self.last_login=="Challenge":
                                            open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;CHALLENGE_OBJECT<Enum 660-900>\n")
                                            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                                            self.print(f"Failed to re-login as {user}, Account is banned or challenge-required!","error")
                                        elif self.last_login=="BadPassword":
                                            try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;BAD_KEY_OR_PASSWORD<ClientObject 5-7>\n")
                                            except:pass
                                            self.print(f"Failed to re-login as {user}, Password {password} is wrong!","warning")
                                        elif self.last_login=="RateLimit":
                                            try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;HTTP_403_POINTER<HttpService.dll 128-565>\n")
                                            except:pass
                                            self.print(f"Failed to re-login as {user}, IP address is Rate Limited!","warning")
                                        elif failed:
                                            try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;REFUSED_CODE<ClientObject 1156-1296>\n")
                                            except:pass
                                            self.print(f"Failed to re-login as {user}, error code {self.last_login}","warning")
                                        elif self.last_login=="Checkpoint":
                                            try:open(self.activity_log,"a+").write(f"{user};{datetime.datetime.now().strftime('%T %D')};LOGIN;REFUSED_CODE<ClientObject 1156-1296>\n")
                                            except:pass
                                            self.print(f"Failed to re-login as {user}, checkpoint required","error")
                                        else:
                                            continue; 
                                        if not self.is_running:return;"""
                                            
                                except:pass
                                try:
                                    self.add_limited(int(str(self.Limited.cget("text")).split("\n")[-1])+1)
                                except:pass
                                break
                try:self.browser.close()
                except:pass
                if self.settings_.shutDown:
                    try:
                        ctypes.WinDLL('user32').ExitWindowsEx(0x00000008, 0x00000000)
                    except Exception:
                        os.system("shutdown /s /t 1")
                elif self.settings_.closeDown:
                    break;
            self.is_running=not self.is_running
        except Exception as e:
            messagebox.showerror("Fatal",traceback.format_exc(),parent=self.root)
            

    def sleep(self,int_:int):
        for n in range(int(int_)):
            time.sleep(1)
            if not self.is_running:sys.exit()
            if n%random.randint(20,60)==0:
                try:
                    self.client.new_feed_exist()
                except:pass
            if len(self.settings_.receivers)<1:
                self.print(f"Receiver list finished, stopping","log")
                self.is_running=not self.is_running
                sys.exit()

    def extractor(self):
        self.client=Client(
        )
        self.client.challenge_code_handler=self.manual_input_code
        self.extract_root=Toplevel(self.root)

        self.extract_root.config(background="white")
        self.extract_root.title("Extractor - GrowDM")
        self.extract_root.geometry("720x480")

        self.user_pass_frame=Frame(self.extract_root)
        self.user_pass_frame.pack(side=TOP,fill=X)

        Label(self.user_pass_frame,text="Username").pack(side=LEFT)
        self.username_extractor_entry=Entry(self.user_pass_frame)
        self.username_extractor_entry.pack(side=LEFT,expand=True)
        Label(self.user_pass_frame,text="Password").pack(side=LEFT)
        self.password_extractor_entry=Entry(self.user_pass_frame)
        self.password_extractor_entry.pack(side=LEFT,expand=True)

        self.target_amount_frame=Frame(self.extract_root)
        self.target_amount_frame.pack(side=TOP,fill=X)
        self.typetarget=StringVar(self.root,"Follower")
        Label(self.target_amount_frame,text="Target").pack(side=LEFT)
        self.target_name=Entry(self.target_amount_frame)
        self.target_name.pack(side=LEFT,expand=True)
        OptionMenu(self.target_amount_frame,self.typetarget,"Follower","Following","Hashtag").pack(side=LEFT)
        Label(self.target_amount_frame,text="Amount").pack(side=LEFT)
        self.amount_entry=Entry(self.target_amount_frame)
        self.amount_entry.pack(side=LEFT,expand=True)

        Button(self.extract_root,text="Start",command=lambda:Thread(target=self.extract).start()).pack(side=TOP,fill=X)

        self.user_extracted=Text(self.extract_root)
        self.user_extracted.pack(fill=BOTH,expand=True,side=TOP)

    def extract(self):
        if not self.amount_entry.get().isdigit():
            messagebox.showwarning(
                "Missing", "Missing data, check again and retry")
            return
        username=self.username_extractor_entry.get()
        password=self.password_extractor_entry.get()
        type_target=self.typetarget.get()
        amount=int(self.amount_entry.get())
        name=self.target_name.get()
        if username=="" or password=="" or name=="":
            messagebox.showwarning("Missing","Missing data, check again and retry")
            return
        self.print(f"Logging in as {username}")
        try:
            self.add_login(int(str(self.Totallogin.cget("text")).split("\n")[-1])+1)
            try:
                self.client.load_settings(self.base_dir+f"{username}.json")  # type: ignore
            except:pass
            self.last_login=self.login(username,password)
            try:
                self.client.dump_settings(self.base_dir+f"{username}.json")  # type: ignore
            except:pass
        except Exception as e:
            self.last_login="Failed"
        if self.last_login=="Challenge":
            self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
            self.print(f"Failed to login as {username}, Account is banned!","error")
            return
        elif self.last_login=="BadPassword":
            self.print(f"Failed to login as {username}, Password {password} is wrong!","warning")
            return
        elif self.last_login=="RateLimit":
            self.print(f"Failed to login as {username}, IP address is Rate Limited!","warning")
            return
        elif self.last_login=="Failed":
            self.print(f"Failed to login as {username}, no status avaiable","warning")
            return
        elif self.last_login=="Checkpoint":
            self.print(f"Failed to login as {username}, checkpoint required","error")
            return
        else:
            self.print(f"ok login for {username}")
        max_id:str=""
        while amount>0:
            self.print("extracting 200 users...")
            if type_target=="Follower":
                try:
                    users,max_id=self.client.user_followers_v1_chunk(self.client.user_id_from_username(name),max_amount=200,max_id=max_id)
                except:
                    self.print(traceback.format_exc(),"warning")
                    break
            if type_target == "Following":
                try:
                    users,max_id=self.client.user_following_v1(self.client.user_id_from_username(name),amount=200,max_id=max_id)
                except:
                    self.print(traceback.format_exc(),"warning")
                    break;
            if type_target=="Hashtag":
                try:
                    users,max_id=self.client.hashtag_medias_v1_chunk(name,tab_key="recent",max_amount=200,max_id=max_id)
                except:
                    self.print(traceback.format_exc(),"warning")
                    break;
            amount-=200
            open(self.base_dir+f"{username}_extracted.txt","a").write("\n".join([i.username for i in users]))
        self.print("done extracting users")

    def filterer_keyword_close(self):
        self.kw_is_closed=True
        self.kw_root.destroy()
    def filterer_keyword(self):
        self.client=Client(        )
        self.client.challenge_code_handler=self.manual_input_code
        self.kw_root=Toplevel(self.root)

        self.kw_is_closed=False

        self.kw_root.config(background="white")
        self.kw_root.protocol("WM_DELETE_WINDOW",self.filterer_keyword_close)
        self.kw_root.title("Keyword filterer - GrowDM")
        self.kw_root.geometry("720x480")

        self.user_pass_frame=Frame(self.kw_root)
        self.user_pass_frame.pack(side=TOP,fill=X)

        Label(self.user_pass_frame,text="Username").pack(side=LEFT)
        self.username_kw_entry=Entry(self.user_pass_frame)
        self.username_kw_entry.pack(side=LEFT,expand=True)
        Label(self.user_pass_frame,text="Password").pack(side=LEFT)
        self.password_kw_entry=Entry(self.user_pass_frame)
        self.password_kw_entry.pack(side=LEFT,expand=True)

        self.target_keyword_list=[]

        self.target_amount_frame=Frame(self.kw_root)
        self.target_amount_frame.pack(side=TOP,fill=X)
        Button(self.target_amount_frame,text="Target",command=self.target_keyword_func).pack(side=LEFT)
        Label(self.target_amount_frame,text="Keyword on Biography/external URL").pack(side=LEFT)
        self.keyword_entry=Entry(self.target_amount_frame)
        self.keyword_entry.pack(side=LEFT,expand=True)

        Button(self.kw_root,text="Start",command=lambda:Thread(target=self.filterer_keyword_main_func).start()).pack(side=TOP,fill=X)

        self.user_extracted=Text(self.kw_root)
        self.user_extracted.pack(fill=BOTH,expand=True,side=TOP)

    def target_keyword_func(self):
        try:
            self.target_keyword_list=open(filedialog.askopenfilename(filetypes=[("Text document",".txt"),("Any file","*.*")]),"r").read().splitlines()
        except:
            messagebox.showerror("Error","Cannot load user list")

    def filterer_keyword_main_func(self):
        try:
            username=self.username_kw_entry.get()
            password=self.password_kw_entry.get()
            keyword=self.keyword_entry.get()
            if username=="" or password=="" or keyword=="" or (len(self.target_keyword_list)==0):
                messagebox.showwarning("Missing","Missing data, check again and retry")
                return
            self.print(f"Logging in as {username}")
            try:
                self.add_login(int(str(self.Totallogin.cget("text")).split("\n")[-1])+1)
                try:
                    self.client.load_settings(self.base_dir+f"{username}.json")  # type: ignore
                except:pass
                self.last_login=self.login(username,password)
                try:
                    self.client.dump_settings(self.base_dir+f"{username}.json")  # type: ignore
                except:pass
            except:
                self.last_login="Failed"
            if self.last_login=="Challenge":
                self.add_banned(int(str(self.banned.cget("text")).split("\n")[-1])+1)
                self.print(f"Failed to login as {username}, Account is banned!","error")
                return
            elif self.last_login=="BadPassword":
                self.print(f"Failed to login as {username}, Password {password} is wrong!","warning")
                return
            elif self.last_login=="RateLimit":
                self.print(f"Failed to login as {username}, IP address is Rate Limited!","warning")
                return
            elif self.last_login=="Failed":
                self.print(f"Failed to login as {username}, no status avaiable","warning")
                return
            elif self.last_login=="Checkpoint":
                self.print(f"Failed to login as {username}, checkpoint required","error")
                return
            else:
                self.print(f"ok login for {username}")
            for user in self.target_keyword_list:
                try:
                    self.user_object=self.client.user_info_v1(
                        str(user) if str(user).isdigit() else 
                            self.client.search_users(str(user))[0].pk)
                    if keyword in str(self.user_object.biography) or keyword in str(self.user_object.external_url):
                        if not os.path.exists("User-downloaded.csv"):
                            open("User-downloaded.csv","w",encoding="utf8").write("sep=;\nUsername;Name;Followers;Followings;Posts;Email;Phone;Verified;Business;Biography;Url")
                        open("User-downloaded.csv","a+",encoding="utf8").write(f"{self.user_object.username};{self.user_object.full_name};{self.user_object.follower_count};{self.user_object.following_count};{self.user_object.media_count};{self.user_object.public_email};{self.user_object.public_phone_country_code}-{self.user_object.public_phone_number};{self.user_object.is_verified};{self.user_object.is_business};"+str(self.user_object.biography).replace("\n","")+f";{self.user_object.external_url}\n")
                        self.print(f"Found user {self.user_object.username} - {self.user_object.full_name}")
                        open("Filtered.txt","a+",encoding="utf8").write(f"{self.user_object.username}\n")
                    try:
                        if self.kw_is_closed:
                            break
                    except:pass
                except exceptions.ChallengeRequired:
                    self.print("Account Banned","error")
                    break
                except exceptions.ChallengeUnknownStep:
                    self.print("Account Banned","error")
                    break
                except exceptions.ChallengeError:
                    self.print("Account Banned","error")
                    break
                except Exception as e:
                    if "feedback_required" in str(e):
                        self.print(f"Account is limited from loading users {e}","error")
                        break
                    if "checkpoint_required" in str(e):
                        self.print(f"SMS/Email ID verification required {e}","error")
                        break
                    else:self.print(f"Error {e}","error")

        except Exception as e:
            self.print(f"Error while executing keyword filterer {e}")

    def login(self,user:str,pass_:str):
        try:
            response,cookies=None,None
            if response=="OK":
                try:
                    if not self.settings_.browser:
                        self.client.private.cookies.update({"csrftoken":cookies["csrftoken"]})
                        self.client.private.cookies.update({"datr":cookies["datr"]})
                        self.client.private.cookies.update({"ig_did":cookies["ig_did"]})
                        self.client.private.cookies.update({"mid":cookies["mid"]})
                        self.client.private.headers.update({"X-MID":cookies["mid"]})
                        self.client.set_ig_u_rur(cookies["rur"])
                except:pass
                self.client.login(user,pass_)
                self.print(f"Login process ended successfully from browser to API for {self.client.username}")
                return "Ok"
            self.client.login(user,pass_)
            try:
                self.client.new_feed_exist()
            except exceptions.LoginRequired:
                self.client = Client()
                self.client.login(user,pass_)
            except:
                if self.settings_.browser:
                    self.client.settings["authorization_data"]={}
                self.client.login(user,pass_)
            try:
                id_=self.client.private_request("session/login_activity/",params={"device_id":self.client.android_device_id})["sessions"][0]["login_id"]
                status=self.client.private_request("session/login_activity/avow_login/",data={"login_id":id_})
                self.print(f"Approve login {status}")
            except exceptions.LoginRequired:
                self.client.settings={}
                self.client.login(user,pass_)
            except Exception as e:pass
            self.print(f"Login process ended successfully")
            return "Ok"
        except exceptions.BadPassword:
            return "BadPassword"
        except exceptions.ChallengeRequired:
            return "Challenge"
        except exceptions.ChallengeSelfieCaptcha:
            return "Challenge"
        except exceptions.ChallengeUnknownStep:
            return "Challenge"
        except exceptions.RateLimitError:
            return "RateLimit"
        except Exception as e:
            if "checkpoint_required" in str(e).lower():
                return "Checkpoint"
            elif "challenge" in str(e).lower():
                return "Challenge"
            return "Failed"

if __name__=="__main__":
    App()
