def is_planning_permission_required(location, height, constraints, other_factors):
    """
    Determines if planning permission is required based on the given parameters.

    Parameters:
    - location: A string indicating the location type.
    - height: A float or int representing the height of the structure.
    - constraints: A set of constraints that may affect planning permission.
    - other_factors: A set of other factors that may affect planning permission.

    Returns:
    - True if planning permission is required, False otherwise.
    """

    # Universal Categories Check
    # Planning permission is required if adjacent to a highway and height is above 1 meter
    if location == 'adjacent to highway' and height > 1:
        return True

    # Planning permission is required if facing a listed building
    if location == 'facing listed building':
        return True

    # Planning permission is required if height is greater than 2 meters
    if height > 2:
        return True

    # Planning Constraints Check
    planning_constraints = {
        'listed building',
        'Article 2(3) Land',
        'Article 2(4) Land',
        'Article 4 Directive',
        'AONB',
        'TPO'
    }

    # Check if any planning constraints require permission
    if constraints.intersection(planning_constraints):
        return True

    # Other Factors Check
    other_constraints = {
        'permitted development rights removed',
        'new build property restrictions'
    }

    # Check if any other factors require permission
    if other_factors.intersection(other_constraints):
        return True

    # Check Other Categories
    if check_other_categories(location, height, constraints):
        return True

    # If none of the above conditions apply, no planning permission is required
    return False


def check_other_categories(location, height, constraints):
    """
    Checks other categories based on provided details for planning permission requirement.

    Returns:
    - True if any condition in other categories requires permission, False otherwise.
    """
    # 2A1 - Planning permission is required if adjacent to highway and height > 1
    if location == 'adjacent to highway' and height > 1:
        return True

    # 2A2 - Planning permission is required if height is above 2 meters
    if height > 2:
        return True

    # 2A3 - Planning permission is required if any significant constraint applies
    planning_constraints = {
        'listed building',
        'Article 2(3) Land',
        'Article 2(4) Land',
        'Article 4 Directive',
        'AONB',
        'TPO'
    }

    if constraints.intersection(planning_constraints):
        return True

    # 2A4 - Planning permission is not required if height <= 2 and no constraints
    if height <= 2 and not constraints.intersection(planning_constraints):
        return False

    # Return false if no specific condition requiring planning permission is met
    return False


# Example 1: Adjacent to highway and height below 1 meter
# Expected: False
location = 'adjacent to highway'
height = 0.9
constraints = set()
other_factors = set()
permission_required = is_planning_permission_required(location, height, constraints, other_factors)
print("Example 1 - Planning Permission Required:", permission_required)

# Example 2: Facing listed building with specific constraints
# Expected: True
location = 'facing listed building'
height = 1.5
constraints = {'listed building', 'Article 4 Directive'}
other_factors = set()
permission_required = is_planning_permission_required(location, height, constraints, other_factors)
print("Example 2 - Planning Permission Required:", permission_required)

# Example 3: In AONB with height less than 2 meters
# Expected: True
location = 'not adjacent to highway'
height = 1.8
constraints = {'AONB'}
other_factors = set()
permission_required = is_planning_permission_required(location, height, constraints, other_factors)
print("Example 3 - Planning Permission Required:", permission_required)

# Example 4: No constraints and height less than 2 meters
# Expected: False
location = 'not adjacent to highway'
height = 1.5
constraints = set()
other_factors = set()
permission_required = is_planning_permission_required(location, height, constraints, other_factors)
print("Example 4 - Planning Permission Required:", permission_required)
