#include <unistd.h>
#include <fcntl.h>

void display_file(char * filename) {
    int fd = open(filename, O_RDONLY);
    if (fd == -1) {
        return;
    }
    char buffer[4096];
    ssize_t bytes_read;
    while ((bytes_read = read(fd, buffer, sizeof(buffer))) > 0) {
        write(STDOUT_FILENO, buffer, bytes_read);
    }
    close(fd);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        return 0;
    }
    int i = 1;
    while (i < argc) {
        display_file(argv[i]);
        i++;
    }
    return 0;
}