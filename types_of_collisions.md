
Find sprites in a group that intersect another sprite.
spritecollide(sprite, group, dokill, collided = None) -> Sprite_list

test if a sprite intersects anything in a group.
spritecollideany(sprite, group, collided = None) -> Sprite

Find all sprites that collide between two groups.
groupcollide(group1, group2, dokill1, dokill2, collided = None) -> Sprite_dict

Collision detection between two sprites, using rects.
collide_rect(left, right) -> bool

test if a point is inside a rectangle
collidepoint(x, y) -> bool