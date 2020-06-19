/**
* Parameters: buffer (pointer to a 100 character buffer)
*             num    (4 byte int)
*
* Description: Writes a string to buffer containing num's value written in decimal, hexadecimal
* (left padded with 0s to be 8 characters wide and prefixed with 0x), then it's hexadecimal
* value printed in little-endian (also left padded and prefixed).  These fields should
* appear in order as listed and be separated by | (the pipe character).
*/
int put_stuff_in_buffer(char* buffer, int num) {
    int a=num>>24;
    int b=num >>8;
    int c=num<<8;
    int d=num<<24;
    int n=((a & 0x000000ff) | (b & 0x0000ff00) | (c & 0x00ff0000) | (d & 0xff000000));
    sprintf(buffer, "%d|0x%.8x|0x%.8x",num,num,n);
   // puts(buffer); 
    return 0;
}
