# Django User Permissions and Groups

## Custom Permissions
We added four custom permissions to the `Book` model:
- `can_view`: Allows viewing the book list.
- `can_create`: Allows adding new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

## Groups and Assigned Permissions
We created three groups:
- **Viewers**: Can only view books.
- **Editors**: Can create and edit books.
- **Admins**: Can perform all actions.

## Enforcing Permissions in Views
We use Django’s `@permission_required` decorator in views to ensure users have the right permissions before performing actions.

## Testing
To test permissions:
1. Create users and assign them to groups in the Django admin panel.
2. Log in as each user and try accessing different views.

