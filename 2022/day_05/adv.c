/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   adv.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bguyot <bguyot@student.42mulhouse.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/10 00:31:08 by bguyot            #+#    #+#             */
/*   Updated: 2022/12/10 00:41:22 by bguyot           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../libft/libft.h"
#include <fcntl.h>

#define NB_STACKS 9

void	move_last_element(
			t_list **stacks,
			int src_id, int dst_id,
			int number_to_move
			);

int	main(void)
{
	int		fd;
	int		index;
	t_list	*stacks[NB_STACKS];
	char	*line;
	char	**split;
	t_list	*lst;

	fd = open("./input", O_RDONLY);
	line = get_next_line(fd);
	index = NB_STACKS;
	ft_bzero(stacks, sizeof (t_list *) * NB_STACKS);
	while (ft_strcmp(line, "\n"))
	{
		index = NB_STACKS;
		while (index--)
		{
			if (ft_isalpha(*(line + 1 + index * 4)))
				ft_lstadd_front(
					stacks + index,
					ft_lstnew(ft_strgen(*(line + 1 + index * 4), 1)));
		}
		free(line);
		line = get_next_line(fd);
	}
	free(line);
	line = get_next_line(fd);
	index = 0;
	while (line)
	{
		split = ft_split(line, ' ');
		move_last_element(
			stacks,
			ft_atoi(split[3]) - 1,
			ft_atoi(split[5]) - 1,
			ft_atoi(split[1])
			);
		index = 0;
		while (index < NB_STACKS)
		{
			lst = stacks[index];
			while (lst) {
				ft_printf("%s->", (char *) lst->content);
				lst = lst->next;
			}
			ft_printf("\n");
			index++;
		}
		ft_printf("---\n");
		free(line);
		line = get_next_line(fd);
	}
	close(fd);
	index = 0;
	while (index < NB_STACKS)
	{
		if (ft_lstlast(*(stacks + index)))
			ft_printf("%s", (char *) ft_lstlast(*(stacks + index))->content);
		else
			ft_printf(" ");
		ft_lstclear(stacks + index, *free);
		index++;
	}
}

void	move_last_element(
	t_list **stacks,
	int src_id,
	int dst_id,
	int number_to_move
	)
{
	t_list	*src;
	t_list	*dst;

	src = *(stacks + src_id);
	dst = *(stacks + dst_id);
	if (ft_lstsize(src) <= number_to_move)
	{
		ft_lstadd_back(stacks + dst_id, src);
		*(stacks + src_id) = NULL;
		return ;
	}
	while (ft_lstsize(src->next) > number_to_move)
		src = src->next;
	ft_lstadd_back(stacks + dst_id, src->next);
	src->next = NULL;
}
