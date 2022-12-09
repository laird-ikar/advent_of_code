#include "../../libft/libft.h"
#include <fcntl.h>

int possibilities[128][128] = {
	['A'] = {
		['X'] = 0 + 3,
		['Y'] = 3 + 1,
		['Z'] = 6 + 2
	},
	['B'] = {
		['X'] = 0 + 1,
		['Y'] = 3 + 2,
		['Z'] = 6 + 3
	},
	['C'] = {
		['X'] = 0 + 2,
		['Y'] = 3 + 3,
		['Z'] = 6 + 1
	}
};

int main()
{
	int		fd;
	int		score;
	char	*line;
	char	**round;

	fd = open("./input", O_RDONLY);
	line = get_next_line(fd);
	score = 0;
	while (line)
	{
		round = ft_split(line, ' ');
		score += possibilities[round[0][0]][round[1][0]];
		free(round[0]);
		free(round[1]);
		free(round);
		free(line);
		line = get_next_line(fd);
	}
	ft_printf("You shall score a total of %d points", score);
	return (0);
}
