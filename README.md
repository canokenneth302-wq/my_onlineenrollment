# Session Isolation

This application provides complete session isolation for each user. Here's how it works:

## How It Works

1. **Unique Session Tokens**: Each user is assigned a unique, cryptographically random session token upon login.
2. **Isolated Storage**: Session data is stored in a way that ensures one user's session data is never accessible to another user.
3. **Token Validation**: Every request is validated against the session token to ensure the user is accessing only their own session data.

## Security Features

- Sessions are automatically invalidated upon logout
- Session tokens expire after a period of inactivity
- All session data is encrypted at rest
