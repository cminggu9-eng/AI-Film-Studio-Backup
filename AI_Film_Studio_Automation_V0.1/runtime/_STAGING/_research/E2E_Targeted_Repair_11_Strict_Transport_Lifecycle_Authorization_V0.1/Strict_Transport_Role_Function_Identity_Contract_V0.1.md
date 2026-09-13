# Strict Transport Role Function Identity Contract V0.1

Authorization is the conjunction of role identity and function identity:

- `Scene Writer` plus `submit_scene_writer_package`: allowed.
- `Director` plus `submit_director_package`: allowed.
- Scene Writer plus the Director function, Director plus the Scene Writer function, unknown functions, unknown roles, and all other strict roles: fail closed.

The registry does not change role semantics, schemas, prompts, canonical Skills, or DeepSeek adapter behavior.
