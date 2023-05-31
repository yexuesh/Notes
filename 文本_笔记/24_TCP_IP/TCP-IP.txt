# TCP/IP网络编程

# 一. 基本流程 

## 1.1 服务器端

```c
#include <sys/socket.h>
socket();  // 创建套接字
bind();  // 分配套接字地址. 分配IP地址 和 端口号
listen();  // 等待连接请求状态. 转化为可接受请求状态
accept();  // 允许连接. 受理连接请求
read() / write();  // 数据交换
close();  // 断开连接
```

## 1.2 客户端

```c
socket();  // 创建套接字
connect();  // 发送连接请求
```

# 二. API函数接口

## 2.1 Winsock的初始化

```c
#include <winsock2.h>
int WSAStartup(WORD wVersionRequested, LPWSADATA lpWSAData);
/*
 * 初始话Winsock
 * wVersionRequested: Winsock版本信息
 * lpWSAData: WSADATA结构体变量的地址值
 * 注: LPWSADATA: WSADATA的指针类型
*/
MAKEWORD(int mainVersion, int deputyVersion);
/*
 * 构建WORD型版本信息
 * mainVersion: 主版本
 * deputyVersion: 副版本
*/
int WSACleanup(void);
/*
 * 注销该库
*/

int main(int argc, char* argv[])
{
    WSADATA wsaData;
    if ( WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
        ErroeHandling(...);
    return 0;
}
```

## 2.2 套接字相关函数

### 2.2.1 创建套接字

```c
// Linux
#include <sys/socket.h>
int socket(int domain, int type, int protocol);  
/*
 * 创建套接字
 * domain: 套接字的 协议族. (Protocol Family)
 * type: 套接字的 数据传输类型. (TCP/UDP . 面向连接/面向消息)
 * protocol: 计算机间通信中 使用的协议信息. (具体协议)
 *
 * domain(Protocol Family):
 	PF_INET(pf_inet)     IPv4
 	PF_INET6(pf_inet6)   IPv6
 	PF_LOCAL(pf_local)   本地通信的UXIX协议族
 	PF_PACKET(pf_packet) 底层套接字的协议族
 	PF_IPX(pf_ipx)       IPX Novell协议族
 * type(套接字类型): 
 	SOCK_STREAM, SOCK_DGRAM(sock_stream, sock_dgram)
 	面向连接(SOCK_STREAM)
 		数据不会消失，按序传输，不存在数据边界(即: IO函数的调用次数无意义, 一次性全部接受)
 	面向消息(SOCK_DGRAM)
 		快速，乱序，不可靠，有数据边界，限制传输数据大小
 * protocol:
 	TCP:
 		int tcp_socket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
 	UDP:
 		int udp_socket = socket(PF_INET, SOCK_DGRAM, IPPROTO_UDP);
*/

listen();  // 等待连接请求状态. 转化为可接受请求状态
accept();  // 允许连接. 受理连接请求
read() / write();  // 数据交换
close();  // 断开连接

// Windows
#include <winsock2.h>

SOCKET socket(int af, int type, int protocol);
int bind(SOCKET s, const struct sockaddr* name, int namelen);
int listen(SOCKET s, int backlog);
SOCKET accept(SOCKET s, struct sockaddr* addr, int* addrlen);
int closesocket(SOCKET s);

int connect(SOCKET s, const struct sockaddr* name, int namelen);
```

### 2.2.2 分配套接字地址(IP地址、端口号)

```c
#include <sys/socket.h>

int bind(int sockfd, struct sockaddr* myaddr, socklen_t addrlen);
/*
 * 分配套接字地址(IP地址、端口号)
 * sockfd: 套接字文件描述符.
 * myaddr: 存有地址信息的结构体. 
 	一般将&struct sockaddr_in 强制转化为 struct sockaddr*.
 	(struct sockaddr*)&struct sockaddr_in 
 * addrlen: ↑ 的长度
*/
```

### 2.2.3 进入等待连接请求状态

```c
#include <sys/socket.h>

int listen(int sock, int backlog);
/*
 * 进入等待连接请求状态
 * sock: 文件描述符. 该文件描述符成为服务器端套接字(监听套接字)
 * backing: (最大)连接请求等待队列长度.
*/
```

### 2.2.4 受理客户端连接请求

```c
int accept(int sock. struct sockaddr* addr, socklen_t* addrlen);
/*
 * 受理客户端连接请求
 * sock: 文件描述符
 * addr: 保存 发起连接请求的客户端的 地址信息的 变量的地址.调用后填充 客户端地址信息
 * addrlen: 保存 ↑ 结构体的长度. 调用后填充
 * @return: 用于数据I/O的套接字的文件描述符. 即 服务器段套接字 单独创建套接字 进行数据交换
*/
```

### 2.2.5 发起连接请求

```c
int connect(int sock, struct sockaddr* servaddr, socklen_t addrlen);
/*
 * 发起连接请求
 * sock: 套接字文件描述符
 * servaddr: 目标服务器端地址信息
 * addrlen: ↑ 的长度
 * 
 * 注: 
 	发生以下情况之一时返回:
 		1. 服务器端接受连接请求
 		2. 断网等异常情况而中断连接请求
 	接受连接请求仅仅是: 将连接请求添加到等待队列
 	该函数自动为客户端分配 IP、端口
*/
```



## 2.3 数据交换

```c
// Linux
/*
 * 分配给标准输入、输出、错误的文件描述符
 * 0 标准输入: Standard Input
 * 1 标准输出: Standard Output
 * 2 标准错误: Standard Error
*/
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int open(const char* path, int flag);
/*
 * 打开文件
 * path: 文件名 及 路径信息
 * flag: 打开模式
 *
 * flag:
 	O_CREAT(o_creat)    必要时创建文件
 	O_TRUNC(o_trunc)    删除现有数据
 	O_APPEND(o_append)  追加数据
 	O_RDONLY(o_rdonly)  只读
 	O_WRONLY(o_wronly)  只写
 	O_RDWR(o_rdwr)      读写
*/
int close(int fd);
/*
 * 关闭文件
 * fd: 文件描述符
*/
ssize_t write(int fd, const void* buf, size_t nbytes);
/*
 * 写入
 * fd: 文件描述符
 * buf: 保存要传输数据的 缓冲地址值
 * nbytes: 要传输的字节数
 * 
 * size_t: unsigned int
 * ssize_t: signed int
*/
ssize_t read(int fd, void* buf, size_t nbytes);
/*
 * 读取
 * fd: 文件描述符
 * buf: 保存要接受的数据的 缓冲地址值
 * nbytes: 要接受的最大字节数
 * 
 * size_t: unsigned int
 * ssize_t: signed int
*/

// Windows
#include <winsock2.h>

int send(SOCKET s, const char* buf, int len, int flags);
/*
 * 发送数据
 * s: 套接字句柄
 * buf: 保存待传输数据的 缓冲地址
 * len: 要传输的字节数
 * flags: 传输数据时用到的 选项
*/
int recv(SOCKET s, const char* buf, int len, int flags);
/*
 * 接受数据
 * s: 套接字句柄
 * buf: 保存接受数据的 缓冲地址
 * len: 接受的最大字节数
 * flags: 接受数据时用到的 选项
*/

// 注: Linux下也有 send(), recv()函数


// 基于UDP的数据 I/O函数
ssize_t sendto(int sock, void* buff, 
               size_t nbytes, int flags,
               struct sockaddr* to, socklen_t addrlen);
/*
 * 填写地址并发送数据
 * sock: UDP套接字文件描述符
 * buff: 保存待传输数据的缓冲地址值
 * nbytes: ↑ 长度(以字节为单位)
 * flags: 可选参数.没有则为0
 * to: 目标地址信息(地址值)
 * addrlen: ↑ 长度
*/
ssize_t recvfrom(int sock, void* buff, 
               size_t nbytes, int flags,
               struct sockaddr* from, socklen_t addrlen);
/*
 * 填写地址并接受数据
 * sock: UDP套接字文件描述符
 * buff: 保存接受数据的缓冲地址值
 * nbytes: ↑ 长度(以字节为单位)
 * flags: 可选参数.没有则为0
 * from: 发送端地址信息(地址值)
 * addrlen: ↑ 长度
*/
```

## 2.4 地址信息表示

```c
struct sockaddr_in
{
    sa_family_t      sin_family;  // 地址族(Address Family)
    uint16_t         sin_port;    // 16位 TCP/UPD 端口号
    struct in_addr   sin_addr;    // 32位IP地址
    char             sin_zero[8]; // 不使用
}
struct in_addr { in_addr_t  s_addr; /* 32位 IPv4 地址 */ }
/*
 * sin_family: 
 	AF_INET    IPv4
 	AF_INET6   IPv6
*/
struct sockaddr
{
    sa_family_t  sin_family;  // 地址族
    char         sa_data[14]; // 地址信息
}
```

## 2.5 网络字节序与地址变换

大端序: 低位数 -> 高位数.  如: 64->  46 
小端序: 高位数 -> 地位数.  如: 64->  64 
网络字节序: 大端序

```c
unsigned short htons(unsigned short);  // 主机 -> 网络字节序(short). 端口
unsigned short ntohs(unsigned short); // 网络字节序 -> 主机(long). 端口
unsigned long htonl(unsigned long);  // 主机 -> 网络字节序(short). IP地址
unsigned long ntohl(unsigned long); // 网络字节序 -> 主机(long). IP地址

addr.sin_addr.s_addr = htonl(INADDR_ANY); // 自动获取运行服务器端的计算机ip地址(只要端口号一致，就可以通信)
```

## 2.6 字符串 -><- 网络字节序

```c
#include <arpa/inet.h>

in_addr_t inet_addr(const char* string);
/*
 * 字符串类型的IP地址 -> 网络字节序(32位整型数据)
 * 成功: 32位整型数据.  失败: INADDR_NONE 
*/
int inet_aton(const char* string, struct in_addr* addr);  // Windows 中没有
/*
 * 字符串类型的IP地址 -> 网络字节序(32位整型数据), 且将转换后的数据填充到addr中
 * string: 字符串类型的IP地址. 如: 192.168.1.13
 * addr: 将保存转化结果的 in_addr结构体变量的地址
 * @return: 成功: 1. 失败: 0
*/

char* inet_ntoa(struct in_addr adr);
/*
 * 网络字节序(32位整型数据) -> 字符串类型的IP地址
 * 
 * 注: 返回的是 char*, 调用后应 将结果重新分配内存, 否则下一次调用将覆盖结果
*/

// Windows中特有的函数. 与inet_ntoa和inet_addr功能完全相同. P55

// 一般调用流程
struct sockaddr_in addr;
char* serv_ip = "211.217.16.13";
char* serv_port = "9310";
memset(&addr, 0, sizeof(addr));
addr.sin_family = AF_INET;  // 指定地址族
addr.sin_addr.s_addr = inet_addr(serv_ip);  // 基于字符串的 IP地址 初始化
// 为服务器时，可将 ↑ 替换为 ↓ :
// addr.sin_addr.s_addr = inet_addr(INADDR_ANY);
addr.sin_port = htos(atoi(serv_port));  // 基于字符串的 端口号 初始化
```

## 2.7 IP地址 -><-域名

```c
// Linux
#include <netdb.h>

struct hostent* gethostbyname(const char* hostname);  // 通过字符串类型的域名 -> IP地址
struct hostent
{
    char*    h_name;        // 官方域名
    char**   h_aliases;     // 其他域名
    int      h_addrtype;    // IP地址的地址族信息
    int      h_length;      // IP地址的长度
    char**   h_addr_list;   // 域名对应的IP地址(整数形式)
}

struct hostent* gethostbyaddr(const char* addr, socklen_t len, int family);
/*
 * IP地址获取域相关信息
 * addr: 含有IP地址的 in_addr 结构指针
 * len: ↑ 长度(IPv4: 4, IPv6: 16)
 * family: 地址族信息(IPv4: AF_INEF, IPv6: AF_INEF6)
*/

// Windows
#include <winsock2.h>
struct hostent* gethostbyname(const char* name);
struct hostent* gethostbyaddr(const char* addr, int len, int type);

```



# 三. TCP/UDP深入理解

## 3.1 TCP

### 3.1.2 基于TCP的半开闭

```c
// Linux
int shutdown(int sock, int howto);
/*
 * sock: 套接字文件描述符
 * howto: 断开方式
 *
 * howto:
 	SHUT_RD:   断开输入流
 	SHUT_WR:   断开输出流
 	SHUT_RDWR: 断开I/O流
*/

// Windows
int shutdows(SOCKET sock, int howto);
/*
 * sock: 套接字文件描述符
 * howto: 断开方式
 *
 * howto:
 	SD_RECEIVE(receive):   断开输入流
 	SD_SEND(send):   断开输出流
 	SD_BOTH(both): 断开I/O流
*/
```



## 3.2 UDP

### 3.2.1 基于UDP的数据I/O函数

```c
// Linux
// 基于UDP的数据 I/O函数
ssize_t sendto(int sock, void* buff, 
               size_t nbytes, int flags,
               struct sockaddr* to, socklen_t addrlen);
/*
 * 填写地址并发送数据
 * sock: UDP套接字文件描述符
 * buff: 保存待传输数据的缓冲地址值
 * nbytes: ↑ 长度(以字节为单位)
 * flags: 可选参数.没有则为0
 * to: 目标地址信息(地址值)
 * addrlen: ↑ 长度
*/
ssize_t recvfrom(int sock, void* buff, 
               size_t nbytes, int flags,
               struct sockaddr* from, socklen_t addrlen);
/*
 * 填写地址并接受数据
 * sock: UDP套接字文件描述符
 * buff: 保存接受数据的缓冲地址值
 * nbytes: ↑ 长度(以字节为单位)
 * flags: 可选参数.没有则为0
 * from: 发送端地址信息(地址值)
 * addrlen: ↑ 长度
*/

// Windows
int sendto(SOCKET s, const* buf, int len, int flags, const struct sockaddr* to, int tolen);
int recvfrom(SOCKET s, const* buf, int len, int flags, const struct sockaddr* from, int fromlen);
参数一致
```



### 3.2.2 存在数据边界的UDP套接字

connected UDP 和 unconnected UDP
UPD连接阶段:

1. 向UDP住粗IP、端口号
2. 传输
3. 删除IP、端口号信息

```c
// 创建已连接UDP套接字  P113
sock = socket(...);
memset(...);
adr.sin_family = ...;
.
.
.
connect(sock, (struct sockaddr*)&adr, sizeof(adr));    
```



# 四. 其他

## IPv4网络地址分类

A : 网络ID(1字节)  主机ID(3字节). 首字节:  0~127   .  首位以0开始
B : 网络ID(2字节)  主机ID(2字节). 首字节: 128~191.  前2位以10开始
C : 网络ID(3字节)  主机ID(1字节). 首字节: 192~223.  前3位以110开始
D : 网络ID(4字节)  主机ID(0字节). 首字节: 

## 端口

端口号范围 0~65535

0~1023为知名端口

TCP/UDP 端口可为同一个
