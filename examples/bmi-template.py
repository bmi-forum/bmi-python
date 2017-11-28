"""The Basic Model Interface."""

__version__ = '0.2'


class BmiBase(object):

    """Methods that control model execution.

    These BMI functions are critical to plug-and-play modeling because they
    give a calling component fine-grained control over the model execution.
    """

    def initialize(self, filename):
        """Perform startup tasks for the model.

        Perform all tasks that take place before entering the model's time
        loop, including opening files and initializing the model state. Model
        inputs are read from a text-based configuration file, specified by
        `filename`.

        Parameters
        ----------
        filename : str, optional
          The path to the model configuration file.

        Notes
        -----
        Models should be refactored, if necessary, to use a
        configuration file. CSDMS does not impose any constraint on
        how configuration files are formatted, although YAML is
        recommended. A template of a model's configuration file
        with placeholder values is used by the BMI.

        """
        pass

    def update(self):
        """Advance model state by one time step.

        Perform all tasks that take place within one pass through the model's
        time loop. This typically includes incrementing all of the model's
        state variables. If the model's state variables don't change in time,
        then they can be computed by the :func:`initialize` method and this
        method can return with no action.

        """
        pass

    def update_until(self, time):
        """Advance model state until the given time.

        Parameters
        ----------
        time : float
          A model time value.

        See Also
        --------
        update

        """
        pass

    def update_frac(self, time_frac):
        """Advance model state by a fraction of a time step.

        Parameters
        ----------
        time_frac : float
          A fraction of a model time step value.

        See Also
        --------
        update

        """
        pass

    def finalize(self):
        """Perform tear-down tasks for the model.

        Perform all tasks that take place after exiting the model's
        time loop. This typically includes deallocating memory,
        closing files, and printing reports.

        """
        pass


class BmiInfo(object):

    """Methods that get metadata about a model."""

    def get_component_name(self):
        """Name of the component.

        Returns
        -------
        str
          The name of the component.

        """
        pass

    def get_input_var_names(self):
        """List of a model's input variables.

        Input variable names must be `CSDMS Standard Names`_, also
        known as *long variable names*.

        Returns
        -------
        tuple of str
          The input variables for the model.

        Notes
        -----
        Standard Names enable the CSDMS framework to determine whether
        an input variable in one model is equivalent to, or compatible
        with, an output variable in another model. This allows the
        framework to automatically connect components.

        Standard Names do not have to be used within the model.

        .. _CSDMS Standard Names:
           http://csdms.colorado.edu/wiki/CSDMS_Standard_Names

        """
        pass

    def get_output_var_names(self):
        """List of a model's output variables.

        Output variable names must be `CSDMS Standard Names`_, also
        known as *long variable names*.

        Returns
        -------
        tuple of str
          The output variables for the model.

        See Also
        --------
        get_input_var_names

        Notes
        -----
        .. _CSDMS Standard Names:
           http://csdms.colorado.edu/wiki/CSDMS_Standard_Names

        """
        pass


class BmiTime(object):

    """Methods that get time information from a model."""

    def get_start_time(self):
        """Start time of the model.

        Model times should be of type float. The default model start
        time is 0.

        Returns
        -------
        float
          The model start time.

        """
        pass

    def get_current_time(self):
        """Current time of the model.

        Returns
        -------
        float
          The current model time.

        See Also
        --------
        get_start_time

        """
        pass

    def get_end_time(self):
        """End time of the model.

        Returns
        -------
        float
          The maximum model time.

        See Also
        --------
        get_start_time

        """
        pass

    def get_time_step(self):
        """Current time step of the model.

        The model time step should be of type float. The default time
        step is 1.0.

        Returns
        -------
        float
          The time step used in model.

        """
        pass

    def get_time_units(self):
        """Time units of the model.

        Returns
        -------
        float
          The model time unit; e.g., `days` or `s`.

        Notes
        -----
        CSDMS uses the `UDUNITS`_ package developed by Unidata.

        .. _UDUNITS: https://www.unidata.ucar.edu/software/udunits

        """
        pass


class BmiVars(object):

    """Methods that get information about input and output variables.

    These BMI functions obtain information about a particular input or output
    variable. They must accommodate any variable that is returned by the BMI
    methods :func:`~bmi.info.BmiInfo.get_input_var_names` or
    :func:`~bmi.info.BmiInfo.get_output_var_names`.
    """

    def get_var_type(self, var_name):
        """Get data type of the given variable.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        str
          The Python variable type; e.g., ``str``, ``int``, ``float``.

        """
        pass

    def get_var_units(self, var_name):
        """Get units of the given variable.

        Standard unit names, in lower case, should be used, such as
        ``meters`` or ``seconds``. Standard abbreviations, like ``m`` for
        meters, are also supported. For variables with compound units,
        each unit name is separated by a single space, with exponents
        other than 1 placed immediately after the name, as in ``m s-1``
        for velocity, ``W m-2`` for an energy flux, or ``km2`` for an
        area.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        str
          The variable units.

        Notes
        -----
        CSDMS uses the `UDUNITS`_ package from Unidata.

        .. _UDUNITS: http://www.unidata.ucar.edu/software/udunits

        """
        pass

    def get_var_itemsize(self, var_name):
        """Get memory use for each array element, in bytes.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        int
          Item size in bytes.

        """
        pass

    def get_var_nbytes(self, var_name):
        """Get size, in bytes, of the given variable.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        int
          The size of the variable, counted in bytes.

        """
        pass

    def get_var_grid(self, var_name):
        """Get the grid identifier for the given variable.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        int
          The grid identifier.

        See Also
        --------
        bmi.info.BmiInfo.get_input_var_names : Get *var_name* from this
            method or from :func:`~bmi.info.BmiInfo.get_output_var_names`.

        """
        pass


class BmiGetter(object):

    """Get variable values from a model.

    Methods that get variables from a model's state. Often a model's state
    variables are changing with each time step, so getters are called to get
    current values.
    """

    def get_value(self, var_name):
        """Get a copy of the values of the given variable.

        This is a getter for the model, used to access the model's
        current state. It returns a *copy* of a model variable, with
        the return type, size and rank dependent on the variable.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        array_like
          The value of a model variable.

        """
        pass

    def get_value_ref(self, var_name):
        """Get a reference to the values of the given variable.

        This is a getter for the model, used to access the model's
        current state. It returns a *reference* to a model variable,
        with the return type, size and rank dependent on the variable.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        array_like
          A reference to a model variable.

        """
        pass

    def get_value_at_indices(self, var_name, indices):
        """Get values at particular locations.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.
        indices : array_like
          The indices into the variable array.

        Returns
        -------
        array_like
            Value of the model variable at the given location.

        """
        pass


class BmiSetter(object):

    """Set values into a component.

    Methods that set variables of a model's state.
    """

    def set_value(self, var_name, src):
        """Specify a new value for a model variable.

        This is the setter for the model, used to change the model's
        current state. It accepts, through *src*, a new value for a
        model variable, with the type, size and rank of *src*
        dependent on the variable.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.
        src : array_like
          The new value for the specified variable.

        """
        pass

    def set_value_at_indices(self, var_name, indices, src):
        """Specify a new value for a model variable at particular indices.

        Parameters
        ----------
        var_name : str
          An input or output variable name, a CSDMS Standard Name.
        indices : array_like
          The indices into the variable array.
        src : array_like
          The new value for the specified variable.

        """
        pass


class BmiGrid(object):

    """Methods that describe a grid.

    """

    def get_grid_rank(self, grid_id):
        """Get number of dimensions of the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        int
          Rank of the grid.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_size(self, grid_id):
        """Get the total number of elements in the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        int
          Size of the grid.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_type(self, grid_id):
        """Get the grid type as a string.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        str
          Type of grid as a string.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass


# Depending on the type of grid used in a model, only one of
#
# * BmiGridRectilinear,
# * BmiGridUniformRectilinear,
# * BmiGridStructuredQuad, or
# * BmiGridUnstructured
#
# needs to be implemented.
class BmiGridRectilinear(BmiGrid):

    """Methods that describe a rectilinear grid.

    In a 2D rectilinear grid, every grid cell (or element) is a rectangle but
    different cells can have different dimensions. All cells in the same row
    have the same grid spacing in the y direction and all cells in the same
    column have the same grid spacing in the x direction. Grid spacings can
    be computed as the difference of successive x or y values.

    """

    def get_grid_shape(self, grid_id):
        """Get dimensions of the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of int
          The dimensions of the grid.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_x(self, grid_id):
        """Get coordinates of grid nodes in the streamwise direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like of float
          The positions of the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_y(self, grid_id):
        """Get coordinates of grid nodes in the transverse direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like of float
          The positions of the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_z(self, grid_id):
        """Get coordinates of grid nodes in the normal direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like of float
          The positions of the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass


# Depending on the type of grid used in a model, only one of
#
# * BmiGridRectilinear,
# * BmiGridUniformRectilinear,
# * BmiGridStructuredQuad, or
# * BmiGridUnstructured
#
# needs to be implemented.
class BmiGridStructuredQuad(BmiGrid):

    """Methods that describe a structured grid of quadrilaterals.

    """

    def get_grid_shape(self, grid_id):
        """Get dimensions of the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The dimensions of the grid.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_x(self, grid_id):
        """Get coordinates of grid nodes in the streamwise direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The positions of the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_y(self, grid_id):
        """Get coordinates of grid nodes in the transverse direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The positions of the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_z(self, grid_id):
        """Get coordinates of grid nodes in the normal direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The positions of the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass


# Depending on the type of grid used in a model, only one of
#
# * BmiGridRectilinear,
# * BmiGridUniformRectilinear,
# * BmiGridStructuredQuad, or
# * BmiGridUnstructured
#
# needs to be implemented.
class BmiGridUniformRectilinear(BmiGrid):

    """Methods that describe a uniform rectilinear grid.

    In a 2D uniform grid, every grid cell (or element) is a rectangle and all
    cells have the same dimensions. If the dimensions are equal, then the
    grid is a tiling of squares.

    Each of these functions returns information about each dimension of a
    grid. The dimensions are ordered with "ij" indexing (as opposed to "xy").
    For example, the :func:`get_grid_shape` function for the example grid would
    return the array ``[4, 5]``. If there were a third dimension, the length of
    the z dimension would be listed first. This same convention is used in
    NumPy. Note that the grid shape is the number of nodes in the coordinate
    directions and not the number of cells or elements. It is possible for
    grid values to be associated with the nodes or with the cells.

    """

    def get_grid_shape(self, grid_id):
        """Get dimensions of the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The dimensions of the grid.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_spacing(self, grid_id):
        """Get distance between nodes of the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The grid spacing.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_origin(self, grid_id):
        """Get coordinates for the origin of the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The coordinates of the lower left corner of the grid.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass


# Depending on the type of grid used in a model, only one of
#
# * BmiGridRectilinear,
# * BmiGridUniformRectilinear,
# * BmiGridStructuredQuad, or
# * BmiGridUnstructured
#
# needs to be implemented.
class BmiGridUnstructured(BmiGrid):

    """Methods that describe an unstructured grid.

    """

    def get_grid_x(self, grid_id):
        """Get coordinates of grid nodes in the streamwise direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The positions of the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_y(self, grid_id):
        """Get coordinates of grid nodes in the transverse direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The positions of the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_z(self, grid_id):
        """Get coordinates of grid nodes in the normal direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like
          The positions of the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_connectivity(self, grid_id):
        """Get connectivity array of the grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like or int
          The graph of connections between the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_offset(self, grid_id):
        """Get offsets for the grid nodes.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like of int
          The offsets for the grid nodes.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass


class Bmi(BmiBase, BmiInfo, BmiTime, BmiVars, BmiGetter, BmiSetter,
          BmiGridRectilinear, BmiGridUniformRectilinear, BmiGridStructuredQuad,
          BmiGridUnstructured):

    """The complete Basic Model Interface.

    Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

    pass
