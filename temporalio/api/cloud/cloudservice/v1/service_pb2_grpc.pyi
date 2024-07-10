"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc

import grpc

import temporalio.api.cloud.cloudservice.v1.request_response_pb2

class CloudServiceStub:
    """WARNING: This service is currently experimental and may change in
    incompatible ways.
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    GetUsers: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUsersRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUsersResponse,
    ]
    """Gets all known users"""
    GetUser: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserResponse,
    ]
    """Get a user"""
    CreateUser: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateUserRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateUserResponse,
    ]
    """Create a user"""
    UpdateUser: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateUserRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateUserResponse,
    ]
    """Update a user"""
    DeleteUser: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteUserRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteUserResponse,
    ]
    """Delete a user"""
    SetUserNamespaceAccess: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.SetUserNamespaceAccessRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.SetUserNamespaceAccessResponse,
    ]
    """Set a user's access to a namespace"""
    GetAsyncOperation: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetAsyncOperationRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetAsyncOperationResponse,
    ]
    """Get the latest information on an async operation"""
    CreateNamespace: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateNamespaceRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateNamespaceResponse,
    ]
    """Create a new namespace"""
    GetNamespaces: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetNamespacesRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetNamespacesResponse,
    ]
    """Get all namespaces"""
    GetNamespace: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetNamespaceRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetNamespaceResponse,
    ]
    """Get a namespace"""
    UpdateNamespace: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateNamespaceRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateNamespaceResponse,
    ]
    """Update a namespace"""
    RenameCustomSearchAttribute: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.RenameCustomSearchAttributeRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.RenameCustomSearchAttributeResponse,
    ]
    """Rename an existing customer search attribute"""
    DeleteNamespace: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteNamespaceRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteNamespaceResponse,
    ]
    """Delete a namespace"""
    FailoverNamespaceRegion: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.FailoverNamespaceRegionRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.FailoverNamespaceRegionResponse,
    ]
    """Failover a multi-region namespace"""
    AddNamespaceRegion: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.AddNamespaceRegionRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.AddNamespaceRegionResponse,
    ]
    """Add a new region to a namespace"""
    GetRegions: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetRegionsRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetRegionsResponse,
    ]
    """Get all regions"""
    GetRegion: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetRegionRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetRegionResponse,
    ]
    """Get a region"""
    GetApiKeys: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetApiKeysRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetApiKeysResponse,
    ]
    """Get all known API keys"""
    GetApiKey: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetApiKeyRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetApiKeyResponse,
    ]
    """Get an API key"""
    CreateApiKey: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateApiKeyRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateApiKeyResponse,
    ]
    """Create an API key"""
    UpdateApiKey: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateApiKeyRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateApiKeyResponse,
    ]
    """Update an API key"""
    DeleteApiKey: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteApiKeyRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteApiKeyResponse,
    ]
    """Delete an API key"""
    GetUserGroups: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserGroupsRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserGroupsResponse,
    ]
    """Get all user groups"""
    GetUserGroup: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserGroupRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserGroupResponse,
    ]
    """Get a user group"""
    CreateUserGroup: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateUserGroupRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateUserGroupResponse,
    ]
    """Create new a user group"""
    UpdateUserGroup: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateUserGroupRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateUserGroupResponse,
    ]
    """Update a user group"""
    DeleteUserGroup: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteUserGroupRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteUserGroupResponse,
    ]
    """Delete a user group"""
    SetUserGroupNamespaceAccess: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.SetUserGroupNamespaceAccessRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.SetUserGroupNamespaceAccessResponse,
    ]
    """Set a user group's access to a namespace"""
    CreateServiceAccount: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateServiceAccountRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateServiceAccountResponse,
    ]
    """Create a service account."""
    GetServiceAccount: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetServiceAccountRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetServiceAccountResponse,
    ]
    """Get a service account."""
    GetServiceAccounts: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetServiceAccountsRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetServiceAccountsResponse,
    ]
    """Get service accounts."""
    UpdateServiceAccount: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateServiceAccountRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateServiceAccountResponse,
    ]
    """Update a service account."""
    DeleteServiceAccount: grpc.UnaryUnaryMultiCallable[
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteServiceAccountRequest,
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteServiceAccountResponse,
    ]
    """Delete a service account."""

class CloudServiceServicer(metaclass=abc.ABCMeta):
    """WARNING: This service is currently experimental and may change in
    incompatible ways.
    """

    @abc.abstractmethod
    def GetUsers(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUsersRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUsersResponse:
        """Gets all known users"""
    @abc.abstractmethod
    def GetUser(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserResponse:
        """Get a user"""
    @abc.abstractmethod
    def CreateUser(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateUserRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateUserResponse:
        """Create a user"""
    @abc.abstractmethod
    def UpdateUser(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateUserRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateUserResponse:
        """Update a user"""
    @abc.abstractmethod
    def DeleteUser(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteUserRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteUserResponse:
        """Delete a user"""
    @abc.abstractmethod
    def SetUserNamespaceAccess(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.SetUserNamespaceAccessRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.SetUserNamespaceAccessResponse:
        """Set a user's access to a namespace"""
    @abc.abstractmethod
    def GetAsyncOperation(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetAsyncOperationRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetAsyncOperationResponse:
        """Get the latest information on an async operation"""
    @abc.abstractmethod
    def CreateNamespace(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateNamespaceRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateNamespaceResponse:
        """Create a new namespace"""
    @abc.abstractmethod
    def GetNamespaces(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetNamespacesRequest,
        context: grpc.ServicerContext,
    ) -> (
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetNamespacesResponse
    ):
        """Get all namespaces"""
    @abc.abstractmethod
    def GetNamespace(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetNamespaceRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetNamespaceResponse:
        """Get a namespace"""
    @abc.abstractmethod
    def UpdateNamespace(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateNamespaceRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateNamespaceResponse:
        """Update a namespace"""
    @abc.abstractmethod
    def RenameCustomSearchAttribute(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.RenameCustomSearchAttributeRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.RenameCustomSearchAttributeResponse:
        """Rename an existing customer search attribute"""
    @abc.abstractmethod
    def DeleteNamespace(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteNamespaceRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteNamespaceResponse:
        """Delete a namespace"""
    @abc.abstractmethod
    def FailoverNamespaceRegion(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.FailoverNamespaceRegionRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.FailoverNamespaceRegionResponse:
        """Failover a multi-region namespace"""
    @abc.abstractmethod
    def AddNamespaceRegion(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.AddNamespaceRegionRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.AddNamespaceRegionResponse:
        """Add a new region to a namespace"""
    @abc.abstractmethod
    def GetRegions(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetRegionsRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetRegionsResponse:
        """Get all regions"""
    @abc.abstractmethod
    def GetRegion(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetRegionRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetRegionResponse:
        """Get a region"""
    @abc.abstractmethod
    def GetApiKeys(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetApiKeysRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetApiKeysResponse:
        """Get all known API keys"""
    @abc.abstractmethod
    def GetApiKey(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetApiKeyRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetApiKeyResponse:
        """Get an API key"""
    @abc.abstractmethod
    def CreateApiKey(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateApiKeyRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateApiKeyResponse:
        """Create an API key"""
    @abc.abstractmethod
    def UpdateApiKey(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateApiKeyRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateApiKeyResponse:
        """Update an API key"""
    @abc.abstractmethod
    def DeleteApiKey(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteApiKeyRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteApiKeyResponse:
        """Delete an API key"""
    @abc.abstractmethod
    def GetUserGroups(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserGroupsRequest,
        context: grpc.ServicerContext,
    ) -> (
        temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserGroupsResponse
    ):
        """Get all user groups"""
    @abc.abstractmethod
    def GetUserGroup(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserGroupRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetUserGroupResponse:
        """Get a user group"""
    @abc.abstractmethod
    def CreateUserGroup(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateUserGroupRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateUserGroupResponse:
        """Create new a user group"""
    @abc.abstractmethod
    def UpdateUserGroup(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateUserGroupRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateUserGroupResponse:
        """Update a user group"""
    @abc.abstractmethod
    def DeleteUserGroup(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteUserGroupRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteUserGroupResponse:
        """Delete a user group"""
    @abc.abstractmethod
    def SetUserGroupNamespaceAccess(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.SetUserGroupNamespaceAccessRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.SetUserGroupNamespaceAccessResponse:
        """Set a user group's access to a namespace"""
    @abc.abstractmethod
    def CreateServiceAccount(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateServiceAccountRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.CreateServiceAccountResponse:
        """Create a service account."""
    @abc.abstractmethod
    def GetServiceAccount(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetServiceAccountRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetServiceAccountResponse:
        """Get a service account."""
    @abc.abstractmethod
    def GetServiceAccounts(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetServiceAccountsRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.GetServiceAccountsResponse:
        """Get service accounts."""
    @abc.abstractmethod
    def UpdateServiceAccount(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateServiceAccountRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.UpdateServiceAccountResponse:
        """Update a service account."""
    @abc.abstractmethod
    def DeleteServiceAccount(
        self,
        request: temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteServiceAccountRequest,
        context: grpc.ServicerContext,
    ) -> temporalio.api.cloud.cloudservice.v1.request_response_pb2.DeleteServiceAccountResponse:
        """Delete a service account."""

def add_CloudServiceServicer_to_server(
    servicer: CloudServiceServicer, server: grpc.Server
) -> None: ...
