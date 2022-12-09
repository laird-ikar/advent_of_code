#include "../../libft/libft.h"
#include <fcntl.h>

void parse_span(int span[2], char *str);

int main()
{
	int		fd;
	int		score;
	int		span[2][2];
	char	**split;
	char	*line;

	fd = open("./input", O_RDONLY);
	line = get_next_line(fd);
	score = 0;
	while (line)
	{
		split = ft_split(line, ',');
		parse_span(span[0], split[0]);
		parse_span(span[1], split[1]);
		score
			+= (span[0][0] >= span[1][0] && span[0][0] <= span[1][1])
			|| (span[0][1] >= span[1][0] && span[0][1] <= span[1][1])
			|| (span[1][0] >= span[0][0] && span[1][0] <= span[0][1])
			|| (span[1][1] >= span[0][0] && span[1][1] <= span[0][1]);
		free(line);
		free(split[0]);
		free(split[1]);
		free(split);
		line = get_next_line(fd);
	}
	close(fd);
	ft_printf("The total of priorities scores of the badges is %d", score);
}

void parse_span(int span[2], char *str)
{
	char **split;

	split = ft_split(str, '-');
	span[0] = ft_atoi(split[0]);
	span[1] = ft_atoi(split[1]);
	free(split[0]);
	free(split[1]);
	free(split);

}
