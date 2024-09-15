### streams
- it is a sequence of data that is being moved from one point to another over time

**Ex:**
- stream of data over the internet being moved from one computer to another
- a stream of data being tranferred from one file to another within the same computer

> [!NOTE]
> in node js the idea is to process streams of data in chunks as they arrive instead of waiting for the entire data to be available before processing
- e:g when you watch a youtube video you don't wait for the whole video to be downloaded to start watching it, the data arrives in chunks and you watch in chunks while the rest of the data arrives over time
- e:g when you are transferring file contents from file1 to file 2, you don't wait for the entire file1 content to be saved in temporary memmory before moving it to file 2 , the contents arrive in chunks and you transfer in chunks while the remaining contents arrive over time

in doing so we prevent unnescessary data downloads and memmory usage

**but how exactly do these sequence of data move?**

### Buffer
- it is an area weher data wait before send to proccessing
- nodejs can't control the pace at which data arrives in the stream
- it can only decide when is the right time to send the data for processing
- if there is data already processed or too little data to process, node puts the arriving data in a buffer
- it is an intentionally small area that node maintains in the runtime to process a stream of data
- e:g when you stream a video online, if your internet connection is fast enough, the speed of the stream will be fast enough to instantly fill up the buffer and send it out for processing, that will repeat till the stream is finished
- if your connection is slow, after processing the first chunk of data taht arrived, the video player will display s aloading spinner which indicates it is waiting for more data to arrive
- once the buffer is filled up and the data is processed, the video player shows the video
- while the video is playing, more data will continue to arrive and wait in the buffer