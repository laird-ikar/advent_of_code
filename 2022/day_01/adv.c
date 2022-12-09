#include "../../libft/libft.h"
#include <fcntl.h>

void compare_top_3(int top_3[3], int value_to_compare);

int main()
{
	int		fd;
	int		max[3];
	int		local_sum;
	char	*str;

	fd = open("./input", O_RDONLY);
	str = get_next_line(fd);
	local_sum = 0;
	ft_bzero(max, sizeof (int) * 3);
	while(str)
	{
		local_sum += ft_atoi(str);
		if (!ft_strcmp(str, "\n"))
		{
			compare_top_3(max, local_sum);
			local_sum = 0;
		}
		str = get_next_line(fd);
	}
	ft_printf("The 3 elves with the most calories got a total of %d calories\n", max[0] + max[1] + max[2]);
}

void compare_top_3(int top_3[3], int value_to_compare)
{
	if (value_to_compare < top_3[2])
		return ;
	if (value_to_compare < top_3[1])
	{
		top_3[2] = value_to_compare;
		return ;
	}
	if (value_to_compare < top_3[0])
	{
		top_3[2] = top_3[1];
		top_3[1] = value_to_compare;
		return ;
	}
	top_3[2] = top_3[1];
	top_3[1] = top_3[0];
	top_3[0] = value_to_compare;
	return ;
}
