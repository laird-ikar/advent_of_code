#include "../../libft/libft.h"
#include <fcntl.h>

int calculate_score(char c);
char	find_duplicate_char(char *str1, char *str2, char *str3);

int main()
{
	int		fd;
	int		score;
	char	*line[3];

	fd = open("./input", O_RDONLY);
	line[0] = get_next_line(fd);
	line[1] = get_next_line(fd);
	line[2] = get_next_line(fd);
	score = 0;
	while (line[0])
	{
		score += calculate_score(find_duplicate_char(line[0], line[1], line[2]));
		free(line[0]);
		free(line[1]);
		free(line[2]);
		line[0] = get_next_line(fd);
		line[1] = get_next_line(fd);
		line[2] = get_next_line(fd);
	}
	close(fd);
	ft_printf("The total of priorities scores of the badges is %d", score);
}

int calculate_score(char c)
{
	if (c >= 'a' && c <= 'z')
		return (c - 'a' + 1);
	if (c >= 'A' && c <= 'Z')
		return (c - 'A' + 27);
	return (0);
}

char	find_duplicate_char(char *str1, char *str2, char *str3)
{
	while (*str1)
	{
		if (ft_strchr(str2, *str1) && ft_strchr(str3, *str1))
			return (*str1);
		str1++;
	}
	return (0);
}
